# Composition root: share the immutable fixture provider through FastAPI dependency injection.
from functools import lru_cache
from app.providers.manifest.in_memory_manifest_provider import InMemoryManifestProvider

@lru_cache(maxsize=1)
def get_manifest_policy() -> InMemoryManifestProvider:
    return InMemoryManifestProvider()
