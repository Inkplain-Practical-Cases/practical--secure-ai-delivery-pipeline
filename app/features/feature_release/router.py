# Thin HTTP door: Pydantic validates inputs, then the handler receives an injected policy.
from fastapi import APIRouter, Depends
from app.core.dependencies import get_manifest_policy
from app.features.feature_release.schemas.release_schemas import ReleaseRequest, ReleaseReceipt
from app.features.feature_release.handlers.handle_validate_release import handle_validate_release
from app.providers.manifest.in_memory_manifest_provider import InMemoryManifestProvider

router = APIRouter(prefix='/release', tags=['release'])

@router.post('/validate', response_model=ReleaseReceipt)
def validate_release(request: ReleaseRequest, policy: InMemoryManifestProvider = Depends(get_manifest_policy)) -> ReleaseReceipt:
    return handle_validate_release(request, policy)
