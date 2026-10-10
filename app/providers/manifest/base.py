# Provider contract: policy can be swapped without modifying the release service.
from typing import Protocol

class ManifestPolicy(Protocol):
    def allowed_versions(self) -> dict[str, str]: ...
