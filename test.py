import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Hello" in res.data

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200