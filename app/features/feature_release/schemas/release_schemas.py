# Release request and receipt contracts; invalid dependency names are rejected at the boundary.
from pydantic import BaseModel, Field

class Dependency(BaseModel):
    name: str = Field(min_length=2, pattern=r'^[a-z][a-z0-9_-]+$')
    version: str = Field(min_length=1, pattern=r'^\d+\.\d+\.\d+$')

class ReleaseRequest(BaseModel):
    service_name: str = Field(min_length=3, pattern=r'^[a-z][a-z0-9-]+$')
    version: str = Field(pattern=r'^\d+\.\d+\.\d+$')
    dependencies: list[Dependency] = Field(min_length=1, max_length=20)
    expected_digest: str | None = Field(default=None, pattern=r'^[a-f0-9]{64}$')

class ReleaseReceipt(BaseModel):
    accepted: bool
    digest: str
    dependency_count: int
