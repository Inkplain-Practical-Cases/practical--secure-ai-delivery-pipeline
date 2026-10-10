# Handler coordinates the validated release request and the injected policy service.
from app.features.feature_release.schemas.release_schemas import ReleaseRequest, ReleaseReceipt
from app.features.feature_release.services.service_validate_release import service_validate_release
from app.providers.manifest.base import ManifestPolicy

def handle_validate_release(request: ReleaseRequest, policy: ManifestPolicy) -> ReleaseReceipt:
    return service_validate_release(request, policy)
