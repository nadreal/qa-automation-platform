import pytest

@pytest.mark.api
def test_create_user(client):    
    user_data = {"id": 1, "name": "Stevan", "role": "user"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    assert response.json() == user_data
   
@pytest.mark.api
def test_list_users(client):
    client.post("/users/", json={"id": 3, "name": "Nidza", "role": "admin"})
    r = client.get("/users/")
    assert r.status_code == 200
    assert len(r.json()) >= 1

@pytest.mark.api
def test_delete_user(client):
    client.post("/users/", json={"id": 4, "name": "Ivan", "role": "user"})
    r = client.delete("/users/4")
    assert r.status_code == 204
    
@pytest.mark.api
def test_get_user(client):    
    user_data = {"id": 1, "name": "Stevan", "role": "user"}
    response = client.post("/users/", json=user_data)
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == user_data
    
@pytest.mark.api_negative
def test_get_missing_user(client):
    r = client.get("/users/999")
    assert r.status_code == 404

@pytest.mark.api_negative
def test_delete_missing_user(client):
    r = client.delete("/users/999")
    assert r.status_code == 404

@pytest.mark.api_negative
def test_duplicate_user(client):
    user = {"id": 10, "name": "Dup", "role": "user"}
    client.post("/users/", json=user)
    r = client.post("/users/", json=user)
    assert r.status_code == 400

@pytest.mark.api
def test_admin_endpoint(client):
    response = client.get("/admin/stats")
    assert response.status_code == 200