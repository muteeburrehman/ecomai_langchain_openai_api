from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_recommend_api():
    payload = {
        "history": "laptops",
        "avg_time": 50,
        "cart_items": "gaming mouse",
        "purchases": "webcam",
        "budget": 250
    }
    response = client.post("/api/recommend", json=payload)
    assert response.status_code == 200
    assert "recommendation" in response.json()
