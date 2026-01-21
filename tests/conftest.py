import pytest

@pytest.fixture
def client():
    from backend.app.dependencies import user_service
    user_service._users.clear()  # reset memory

    from backend.app.main import app
    from fastapi.testclient import TestClient
    return TestClient(app)