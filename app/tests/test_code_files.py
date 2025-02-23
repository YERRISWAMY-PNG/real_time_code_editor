from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_code_file():
    response = client.post("/code-files/", json={"filename": "test.py", "content": "print('Hello, World!')", "owner_id": 1})
    assert response.status_code == 200
    assert response.json()["filename"] == "test.py"