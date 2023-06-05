from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_route_product():
    response = client.get("/product")
    assert response.status_code ==200