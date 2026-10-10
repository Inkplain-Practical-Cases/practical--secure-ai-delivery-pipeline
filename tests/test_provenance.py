# Prevent tag-only deployment and mismatched attestation.
import pytest
from app.features.feature_release.services.service_verify_artifact_provenance import service_verify_artifact_provenance
D='sha256:'+'a'*64

def test_accepts_matching_digest():
    assert service_verify_artifact_provenance('registry.example/agent@'+D,D,D)

def test_rejects_tag_only():
    with pytest.raises(ValueError): service_verify_artifact_provenance('registry.example/agent:latest',D,D)

def test_rejects_mismatched_provenance():
    with pytest.raises(ValueError): service_verify_artifact_provenance('registry.example/agent@'+D,D,'sha256:'+'b'*64)
