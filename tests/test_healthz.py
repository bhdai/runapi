from fastapi.testclient import TestClient

from runapi import app


def test_healthz() -> None:
    response = TestClient(app).get("/healthz")
    assert response.json() == {"status": "ok", "env": "dev"}
