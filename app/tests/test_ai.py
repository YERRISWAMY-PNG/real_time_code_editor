from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_ai_suggestion():
    response = client.post("/ai-suggestions/", json={"code_file_id": 1, "suggestion": "Fix indentation"})
    assert response.status_code == 200
    assert response.json()["suggestion"] == "Fix indentation"