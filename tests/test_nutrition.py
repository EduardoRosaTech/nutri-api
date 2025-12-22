from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_nutrition():
    response = client.post(
        "/nutrition/analyze",
        json={"texto": "arroz, frango"}
    )

    assert response.status_code == 200
    assert response.json()["total_calorias"] == 295
