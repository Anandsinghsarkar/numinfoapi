import os
import secrets
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Hitek API Starter",
    version="1.0.0",
    description="A Vercel-ready FastAPI starter with API-key protection."
)

LANDING_PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hitek API Gateway</title>
<style>
:root{color-scheme:dark}*{box-sizing:border-box}
body{margin:0;min-height:100vh;display:grid;place-items:center;
background:radial-gradient(circle at 20% 20%,#073b39,#050811 55%);
color:#e8fffb;font-family:system-ui,Arial,sans-serif}
.card{width:min(92%,720px);padding:clamp(24px,5vw,52px);border:1px solid #18d9bd;
border-radius:22px;background:#071416dd;box-shadow:0 0 50px #00d9b433}
.badge{color:#52f5d7;font-size:.85rem;letter-spacing:.18em}
h1{font-size:clamp(2rem,7vw,4rem);margin:.6rem 0}
p{color:#b8d0d0;line-height:1.7}.pill{display:inline-block;padding:8px 12px;
border:1px solid #227e73;border-radius:999px;color:#72f8df;margin:5px 5px 0 0}
code{color:#8dffe9}
</style></head>
<body><main class="card">
<div class="badge">H I T E K  /  A P I</div>
<h1>API Gateway Online</h1>
<p>Your FastAPI service is running. Use the health endpoint to check deployment.
Protected endpoints require an API key configured in Vercel environment variables.</p>
<span class="pill">FastAPI</span><span class="pill">Vercel-ready</span>
<span class="pill">API-key protection</span>
<p>Health check: <code>/health</code><br>API documentation: <code>/docs</code></p>
</main></body></html>"""

def require_api_key(x_api_key: str | None) -> None:
    expected = os.getenv("API_KEY")
    if not expected:
        # Fail closed: protected endpoints are unavailable until configured.
        raise HTTPException(status_code=503, detail="API_KEY is not configured")
    if not x_api_key or not secrets.compare_digest(x_api_key, expected):
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

@app.get("/", response_class=HTMLResponse)
def home():
    return LANDING_PAGE

@app.get("/health")
def health():
    return {"status": "ok", "service": "hitek-api"}

@app.get("/api/example")
def example(x_api_key: str | None = Header(default=None)):
    require_api_key(x_api_key)
    return {
        "status": "ok",
        "message": "Authenticated API is working.",
        "data": []
    }

@app.get("/FetchData")
def fetch_data(Number: str, x_api_key: str | None = Header(default=None)):
    # Safe starter endpoint: does not query or expose personal-data datasets.
    require_api_key(x_api_key)
    if not Number.isdigit() or not 10 <= len(Number) <= 15:
        raise HTTPException(status_code=400, detail="Number must contain 10–15 digits")
    return {
        "status": "not_configured",
        "message": "Connect only a dataset you own or are authorized to process.",
        "Data": {"Main_Records": [], "Alt_Records": []}
    }
