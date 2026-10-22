# Hitek API — GitHub + Vercel starter

This repository is a minimal FastAPI project prepared for deployment on Vercel.

## Included endpoints

- `GET /` — landing page
- `GET /health` — deployment health check
- `GET /docs` — FastAPI interactive documentation
- `GET /api/example` — example API protected by an API key
- `GET /FetchData?Number=1234567890` — protected placeholder endpoint

**Privacy note:** The provided starter intentionally does not include the original remote phone-number lookup against Parquet files. Only connect data you own or are explicitly authorized to process, and protect personal data with appropriate access controls.

## Deploy

1. Create a GitHub repository and upload these files.
2. Open Vercel and import that GitHub repository.
3. Deploy with the default settings.
4. In Vercel: **Project → Settings → Environment Variables**, add:
   - Name: `API_KEY`
   - Value: a long, unique random secret
   Apply it to the environments you use, then redeploy.
5. Test `https://YOUR-PROJECT.vercel.app/health`.

## Call the protected endpoint

Send the API key in the `X-API-Key` header. Do not put the key in a public URL or commit it to GitHub.

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
  "https://YOUR-PROJECT.vercel.app/api/example"
```

The `/FetchData` endpoint is only a safe placeholder until you connect an authorized data source. It does not return personal records.

## Local test

```bash
python -m pip install -r requirements.txt
export API_KEY='replace-with-a-long-random-secret'
uvicorn api.index:app --reload
```

On Windows PowerShell, set the environment variable with:

```powershell
$env:API_KEY = "replace-with-a-long-random-secret"
uvicorn api.index:app --reload
```
