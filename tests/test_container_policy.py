# Static safety tests work without Docker credentials or a daemon.
import pytest
from app.features.feature_release.services.service_check_container_policy import service_check_container_policy

def test_real_dockerfile_non_root():
    assert service_check_container_policy('Dockerfile')

def test_root_dockerfile_rejected(tmp_path):
    bad = tmp_path / 'Dockerfile'
    bad.write_text('FROM python:3.12\nUSER root\n')
    with pytest.raises(ValueError):
        service_check_container_policy(str(bad))

def test_secret_build_arg_rejected(tmp_path):
    bad = tmp_path / 'Dockerfile'
    bad.write_text('FROM python:3.12\nARG API_KEY\nUSER 10001\n')
    with pytest.raises(ValueError):
        service_check_container_policy(str(bad))
