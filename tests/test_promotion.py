# Fail-safe decision tests for privileged deployment workflow.
import pytest
from app.features.feature_release.services.service_decide_promotion import service_decide_promotion
from app.features.feature_release.services.service_resolve_rollback import service_resolve_rollback

def test_promotes_verified_and_approved():
    assert service_decide_promotion('release-approver',True,True,True)=='promote'

def test_unhealthy_staging_rolls_back():
    assert service_decide_promotion('release-approver',True,False,True)=='rollback'

def test_unauthorized_rejected():
    with pytest.raises(PermissionError): service_decide_promotion('developer',True,True,True)

def test_unknown_digest_rejected():
    with pytest.raises(ValueError): service_resolve_rollback('sha256:'+'a'*64,set())
