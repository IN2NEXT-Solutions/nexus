from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_not_found_uses_standard_error_shape() -> None:
    response = client.get("/api/v1/does-not-exist")

    assert response.status_code == 404

    body = response.json()

    assert "error" in body
    assert body["error"]["code"] == "HTTP_ERROR"
    assert body["error"]["message"]
    assert body["error"]["request_id"]


def test_validation_error_uses_standard_error_shape() -> None:
    response = client.get("/api/v1/health?unexpected=value")

    assert response.status_code == 200
