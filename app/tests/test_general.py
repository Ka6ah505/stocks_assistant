from fastapi.testclient import TestClient
# from app.api.api_v1 import routes
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "All right!"}
