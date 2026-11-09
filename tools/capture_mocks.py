"""Capture Biohub MCP responses for the eval mocks, signed in as the person running it.

Usage: python3 tools/capture_mocks.py <out-dir>

It registers an OAuth client, opens the Biohub sign-in page in the browser, waits for the
callback on http://127.0.0.1:47200/callback, then records `tools/list` and every call in CALLS.
The access token is held in memory only. Calls marked billed spend the signed-in account's credits.
"""

import base64
import hashlib
import http.server
import json
import random
import secrets
import sys
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

MCP_URL = "https://biohub.ai/mcp"
CALLBACK_PORT = 47200
REDIRECT_URI = f"http://127.0.0.1:{CALLBACK_PORT}/callback"
# Cloudflare in front of Clerk rejects Python's default User-Agent with error 1010.
USER_AGENT = "biohub-skills-mock-capture/0"
GB1 = "MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE"
# A seeded random 800-residue protein, so it has no stored Atlas structure and is over 700 residues.
LONG = "".join(random.Random(0).choices("ACDEFGHIKLMNPQRSTVWY", k=800))


def http_json(url: str, data: dict | None = None, form: bool = False, headers: dict | None = None):
    body = None
    all_headers = {"Accept": "application/json", "User-Agent": USER_AGENT, **(headers or {})}
    if data is not None and form:
        body = urllib.parse.urlencode(data).encode()
        all_headers["Content-Type"] = "application/x-www-form-urlencoded"
    elif data is not None:
        body = json.dumps(data).encode()
        all_headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, body, all_headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode())


def sign_in() -> str:
    resource = http_json("https://biohub.ai/.well-known/oauth-protected-resource/mcp")
    issuer = resource["authorization_servers"][0]
    server = http_json(f"{issuer}/.well-known/oauth-authorization-server")
    client = http_json(
        server["registration_endpoint"],
        {
            "client_name": "biohub-skills eval mock capture",
            "redirect_uris": [REDIRECT_URI],
            "grant_types": ["authorization_code"],
            "response_types": ["code"],
            "token_endpoint_auth_method": "none",
            # The MCP requires openid and email; Clerk grants a new client only the scopes it asks for.
            "scope": "openid email profile",
        },
    )
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=")
    state = secrets.token_urlsafe(16)
    query = urllib.parse.urlencode(
        {
            "response_type": "code",
            "client_id": client["client_id"],
            "redirect_uri": REDIRECT_URI,
            "scope": "openid email",
            "state": state,
            "code_challenge": challenge.decode(),
            "code_challenge_method": "S256",
            "resource": MCP_URL,
        }
    )
    received: dict[str, str] = {}

    class Callback(http.server.BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            received.update({key: values[0] for key, values in params.items()})
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Signed in. You can close this tab.")

        def log_message(self, *args: object) -> None:
            pass

    listener = http.server.HTTPServer(("127.0.0.1", CALLBACK_PORT), Callback)
    sign_in_url = f"{server['authorization_endpoint']}?{query}"
    print(
        f"Opening the Biohub sign-in page; if the tab closes, open it again:\n{sign_in_url}",
        flush=True,
    )
    webbrowser.open(sign_in_url)
    listener.handle_request()
    listener.server_close()
    if received.get("state") != state or "code" not in received:
        raise SystemExit(f"Sign-in did not complete: {received.get('error', 'no code returned')}")
    token = http_json(
        server["token_endpoint"],
        {
            "grant_type": "authorization_code",
            "code": received["code"],
            "redirect_uri": REDIRECT_URI,
            "client_id": client["client_id"],
            "code_verifier": verifier,
            "resource": MCP_URL,
        },
        form=True,
    )
    return token["access_token"]


class Session:
    def __init__(self, token: str) -> None:
        self.headers = {
            "Authorization": f"Bearer {token}",
            "User-Agent": USER_AGENT,
            "Accept": "application/json, text/event-stream",
            "Content-Type": "application/json",
        }
        self.next_id = 1

    def post(self, message: dict) -> dict | None:
        request = urllib.request.Request(MCP_URL, json.dumps(message).encode(), self.headers)
        try:
            response = urllib.request.urlopen(request, timeout=300)
        except urllib.error.HTTPError as error:
            # The auth failure reason is only in the body and WWW-Authenticate header.
            challenge = error.headers.get("WWW-Authenticate", "")
            raise SystemExit(f"MCP {error.code}: {error.read().decode()} {challenge}") from error
        with response:
            if session_id := response.headers.get("Mcp-Session-Id"):
                self.headers["Mcp-Session-Id"] = session_id
            raw = response.read().decode()
            content_type = response.headers.get("Content-Type", "")
        if not raw.strip():
            return None
        if "event-stream" in content_type:
            events = [line[5:].strip() for line in raw.splitlines() if line.startswith("data:")]
            return json.loads(events[-1])
        return json.loads(raw)

    def request(self, method: str, params: dict | None = None) -> dict:
        message = {"jsonrpc": "2.0", "id": self.next_id, "method": method, "params": params or {}}
        self.next_id += 1
        reply = self.post(message)
        if reply is None or "error" in reply:
            raise SystemExit(f"{method} failed: {reply}")
        return reply["result"]


def text_of(result: dict) -> str:
    return "".join(block["text"] for block in result["content"] if block["type"] == "text")


def main() -> None:
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    session = Session(sign_in())
    init = session.request(
        "initialize",
        {
            "protocolVersion": "2025-06-18",
            "capabilities": {},
            "clientInfo": {"name": "biohub-skills-mock-capture", "version": "0"},
        },
    )
    session.post({"jsonrpc": "2.0", "method": "notifications/initialized"})
    (out / "_server.json").write_text(json.dumps(init["serverInfo"], indent=2) + "\n")
    tools = session.request("tools/list")
    (out / "_tools.json").write_text(json.dumps(tools, indent=2, ensure_ascii=False) + "\n")
    print("server", init["serverInfo"], "tools", [tool["name"] for tool in tools["tools"]])

    def call(key: str, tool: str, arguments: dict) -> dict:
        result = session.request("tools/call", {"name": tool, "arguments": arguments})
        record = {"tool": tool, "arguments": arguments, **result}
        (out / f"{key}.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
        print(
            key, "error" if result.get("isError") else "ok", [b["type"] for b in result["content"]]
        )
        return result

    def protein(text: str) -> str:
        return json.loads(text)["proteins"][0]["sequence"]

    hba = protein(
        text_of(
            call(
                "search_uniprot.P69905", "esm_atlas_search_uniprot", {"query": "P69905", "size": 1}
            )
        )
    )
    hbb = protein(
        text_of(
            call(
                "search_uniprot.P68871", "esm_atlas_search_uniprot", {"query": "P68871", "size": 1}
            )
        )
    )
    call(
        "search_uniprot.hemoglobin", "esm_atlas_search_uniprot", {"query": "hemoglobin", "size": 6}
    )
    hits = json.loads(
        text_of(
            call(
                "search_similar.GB1",
                "esm_atlas_search_similar_protein_clusters",
                {"sequence": GB1, "top_k": 10, "uncharacterized_only": False},
            )
        )
    )
    top_hit = hits["hits"][0]["sequence"]
    call("protein_details.GB1", "esm_atlas_get_protein_details", {"sequence": GB1})
    call("cluster_info.top_hit", "esm_atlas_get_cluster_info", {"sequence": top_hit})
    call("sae_feature.13", "esm_atlas_get_sae_feature_detail", {"feature_index": 13})
    call("lookup_accession.P69905", "esm_atlas_lookup_accession", {"accession": "P69905"})
    for key, sequence in (("GB1", GB1), ("P69905", hba), ("top_hit", top_hit), ("long", LONG)):
        call(
            f"view.{key}",
            "ui_show_structure",
            {"entities": [{"type": "protein", "sequence": sequence}]},
        )
    # Billed from here on.
    tetramer = [{"type": "protein", "sequence": s} for s in (hba, hba, hbb, hbb)]
    call("view.hemoglobin_tetramer", "ui_show_structure", {"entities": tetramer})
    call(
        "score.GB1_W43F",
        "esmc_score_mutations",
        {
            "sequence": GB1,
            "mutations": [{"position": 43, "expected_wild_type": "W", "alternate": "F"}],
        },
    )
    call(
        "score.GB1_A43F",
        "esmc_score_mutations",
        {
            "sequence": GB1,
            "mutations": [{"position": 43, "expected_wild_type": "A", "alternate": "F"}],
        },
    )
    call("scan.GB1", "esmc_scan_mutation_tolerance", {"sequence": GB1, "positions": "all"})
    call(
        "fold.hemoglobin_dimer",
        "esmfold2_fold_complex",
        {
            "entities": [
                {"type": "protein", "sequence": hba},
                {"type": "protein", "sequence": hbb},
            ],
        },
    )
    queued = json.loads(
        text_of(
            call(
                "fold.GB1_batch",
                "esmfold2_fold_complex",
                {
                    "entities": [{"type": "protein", "sequence": GB1}],
                    "use_batch_api": True,
                },
            )
        )
    )
    if queued.get("run_id"):
        call("run.GB1_batch", "biohub_get_inference_run", {"run_id": queued["run_id"]})


if __name__ == "__main__":
    main()
