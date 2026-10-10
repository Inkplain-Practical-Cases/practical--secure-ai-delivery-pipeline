# Only runtime references are permitted; no real values appear in fixtures.
import pytest
from app.features.feature_release.services.service_check_secret_policy import service_check_secret_policy

def test_runtime_injection_reference():
    assert service_check_secret_policy({'APP_ENV':'stage'},{'MODEL_API_KEY'})

def test_image_secret_rejected():
    with pytest.raises(ValueError): service_check_secret_policy({'API_KEY':'synthetic-placeholder'},{'MODEL_API_KEY'})
