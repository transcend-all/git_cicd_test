# tests/test_main.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_dev2():
    response = client.get("/dev2")

    assert response.status_code == 200
    assert response.json() == {"status": "dev2"}