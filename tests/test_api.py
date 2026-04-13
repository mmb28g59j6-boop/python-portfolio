from fastapi.testclient import TestClient

from portfolio.api import app


client = TestClient(app)


def test_ping() -> None:
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_echo() -> None:
    response = client.post("/echo", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json() == {"text": "hello"}


def test_add() -> None:
    response = client.post("/add", json={"left": 2, "right": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}
