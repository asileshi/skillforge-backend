from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token(username: str, password: str) -> str:
    client.post("/auth/register", json={"username": username, "password": password})
    response = client.post("/auth/login", json={"username": username, "password": password})
    
    return response.json().get("access_token")

def test_create_skill():
    username = "skill_user_1"
    password = "password123"
    token = get_token(username, password)

    response = client.post(
        "/skills/",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Test Skill", "description": "This is a test skill"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Skill"
    assert data["description"] == "This is a test skill"
    assert "id" in data
    