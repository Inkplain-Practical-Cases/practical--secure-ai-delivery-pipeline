# Deterministic offline dependency policy for the educational release pipeline.
class InMemoryManifestProvider:
    def allowed_versions(self) -> dict[str, str]:
        return {'fastapi': '0.115.12', 'pydantic': '2.11.3'}
