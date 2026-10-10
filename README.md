# Secure AI Delivery Pipeline

Six cumulative teaching branches for a synthetic FastAPI release-validation and supply-chain security reference. This is an educational fixture, not a production registry, deployment orchestrator or signed attestation provider.

| Step | Capability | Branch |
|---|---|---|
| 1 | Release manifest validation | `step-01-release-manifest-validation` |
| 2 | Container image and non-root runtime | `step-02-container-image-and-non-root-runtime` |
| 3 | Immutable artifact and registry provenance | `step-03-immutable-artifact-and-registry-provenan` |
| 4 | Runtime secret policy and leak scanning | `step-04-runtime-secret-policy-and-leak-scanning` |
| 5 | Approval gates staging and rollback | `step-05-approval-gates-staging-and-rollback` |
| 6 | Security regressions and CI matrix | `step-06-security-regressions-and-ci-matrix` |

## Run

```bash
python -m pip install -r requirements.lock
python -m pytest -q
uvicorn app.main:app
```

To inspect step N: `git checkout <step branch>` and read `STEP-N.md`, `STEP-N.crd` and code comments. On main, read FINAL.crd and import `secure-ai-delivery-pipeline.inkp` into the Inkplain Simulator; six tabs model the source components and security policies. Only the supplied sample tests have CI evidence; registry signing, real runtime secret stores and staging systems are outside the fixture.
