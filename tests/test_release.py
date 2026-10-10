# Offline boundary tests for the STEP-1 FastAPI release contract.
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE = {'service_name': 'invoice-agent', 'version': '1.0.0', 'dependencies': [{'name': 'fastapi', 'version': '0.115.12'}]}

def test_stable_digest():
    first = client.post('/release/validate', json=BASE)
    second = client.post('/release/validate', json=BASE)
    assert first.status_code == 200
    assert first.json() == second.json()
    assert len(first.json()['digest']) == 64

def test_unapproved_version():
    body = {**BASE, 'dependencies': [{'name': 'fastapi', 'version': '9.9.9'}]}
    assert client.post('/release/validate', json=body).status_code == 422

def test_duplicate_name():
    body = {**BASE, 'dependencies': BASE['dependencies'] * 2}
    assert client.post('/release/validate', json=body).status_code == 422

def test_digest_mismatch():
    body = {**BASE, 'expected_digest': '0' * 64}
    assert client.post('/release/validate', json=body).status_code == 409

def test_invalid_service_name():
    body = {**BASE, 'service_name': '../private'}
    assert client.post('/release/validate', json=body).status_code == 422
