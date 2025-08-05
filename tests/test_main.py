from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post(
        "/auth/register", 
        json={"username": "testuser3", "password": "testpassword"}
        )
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_user():
    client.post(
        "/auth/register",
        json={"username": "testlogin", "password": "testass"}
    )

    response = client.post(
        "/auth/login",
        json={"username": "testlogin", "password": "testass"}
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"