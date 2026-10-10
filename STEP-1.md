# STEP-1: Validate release manifests

A thin FastAPI door calls the handler, service and injected offline allowlist provider. The service accepts exact versions for approved dependencies, rejects duplicates and computes a deterministic SHA-256 digest from a canonical sorted manifest. This is **not yet** a reproducible container build.

## Run and verify

```bash
python -m pip install -r requirements.lock
python -m pytest -q
uvicorn app.main:app
```

POST `/release/validate` with JSON `{"service_name":"invoice-agent","version":"1.0.0","dependencies":[{"name":"fastapi","version":"0.115.12"}]}`. A valid request returns a 64-character digest. Unapproved dependencies and duplicates return 422; mismatched digests return 409. No external credentials are required.

## Next

STEP-2 will add a reproducible non-root container build and a corresponding cumulative CRD.
