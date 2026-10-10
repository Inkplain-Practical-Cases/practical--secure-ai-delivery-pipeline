# Integrative offline negative cases for the complete supply-chain policy.
import pytest
from app.features.feature_release.services.service_verify_artifact_provenance import service_verify_artifact_provenance
from app.features.feature_release.services.service_check_secret_policy import service_check_secret_policy
from app.features.feature_release.services.service_decide_promotion import service_decide_promotion
D='sha256:'+'c'*64

def test_tag_move_cannot_replace_digest():
    with pytest.raises(ValueError): service_verify_artifact_provenance('registry.test/app:v2',D,D)

def test_build_secret_fails_closed():
    with pytest.raises(ValueError): service_check_secret_policy({'SERVICE_TOKEN':'placeholder'},{'SERVICE_TOKEN'})

def test_failed_test_blocks_promotion():
    assert service_decide_promotion('release-approver',False,True,True)=='hold'
