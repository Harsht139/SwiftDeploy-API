# tests/test_main.py
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API!"}


def test_get_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# in tests/test_main.py


def test_process_item_even():
    response = client.get("/process/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "is_even_or_odd": "even"}


def test_process_item_odd():
    response = client.get("/process/99")
    assert response.status_code == 200
    assert response.json() == {"item_id": 99, "is_even_or_odd": "odd"}


def test_process_item_invalid_id():
    response = client.get("/process/-1")
    assert response.status_code == 400
    assert response.json() == {"detail": "Item ID must be a positive integer."}
