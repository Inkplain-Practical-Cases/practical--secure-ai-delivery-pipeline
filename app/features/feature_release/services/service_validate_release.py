# Pure release verification: reject floating/duplicate/unapproved dependencies and hash canonical bytes.
import hashlib
import json
from fastapi import HTTPException
from app.features.feature_release.schemas.release_schemas import ReleaseRequest, ReleaseReceipt
from app.providers.manifest.base import ManifestPolicy

def service_validate_release(request: ReleaseRequest, policy: ManifestPolicy) -> ReleaseReceipt:
    # Resolve the server-owned allowlist; never trust client-declared approved versions.
    allowed = policy.allowed_versions()
    supplied = [(item.name, item.version) for item in request.dependencies]
    if len(set(name for name, _ in supplied)) != len(supplied):
        raise HTTPException(status_code=422, detail='Duplicate dependency name')
    if any(allowed.get(name) != version for name, version in supplied):
        raise HTTPException(status_code=422, detail='Unapproved or unpinned dependency')
    # Stable ordering and separators make the digest independent of JSON field order.
    manifest = {'service': request.service_name, 'version': request.version, 'dependencies': sorted(supplied)}
    digest = hashlib.sha256(json.dumps(manifest, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    if request.expected_digest is not None and request.expected_digest != digest:
        raise HTTPException(status_code=409, detail='Manifest digest mismatch')
    return ReleaseReceipt(accepted=True, digest=digest, dependency_count=len(supplied))
