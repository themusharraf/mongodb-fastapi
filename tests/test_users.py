from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/users", json={
        "username": "john_doe",
        "firstname": "John",
        "surname": "Doe",
        "birthday": "1990-01-01",
        "region": "Tashkent",
        "studentsId": []
    })
    assert response.status_code == 200
    assert response.json()["username"] == "john_doe"
