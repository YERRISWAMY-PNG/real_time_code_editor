from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "test", "email": "test@example.com", "password": "test", "role": "user"})
    assert response.status_code == 200
    assert response.json()["username"] == "test"