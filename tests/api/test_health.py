import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create():
    # create user
    user_data = {"id": 1, "name": "Stevan", "role": "user"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    assert response.json() == user_data

def test_get_user():
    # get user
    user_data = {"id": 1, "name": "Stevan", "role": "user"}
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == user_data
