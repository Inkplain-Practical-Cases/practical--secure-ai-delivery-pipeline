# STEP-4: Runtime secret policy and leak scanning

Build on previous branch with a separate, deterministic security control. Read each file's teaching comments and test the negative case before trusting the positive case.

## Components and change
- app/features/feature_release/services/service_check_secret_policy.py — added security policy

## Run and verify

```bash
python -m pip install -r requirements.lock
python -m pytest -q
```

Expected: pytest passes; each unauthorized, invalid, or leaked input is rejected by a negative test. Docker, when available: `docker build -t secure-ai-delivery:test .` then `docker run --rm secure-ai-delivery:test id -u` (must not be 0).

## Next
Extend this branch with the next security gate.
