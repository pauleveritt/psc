"""Test the Starlette web app for browsing examples."""
from starlette.testclient import TestClient

from psc.app import app


def test_homepage() -> None:
    """Test the view for the index route."""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200


def test_favicon() -> None:
    """Test the view for the favicon route."""
    client = TestClient(app)
    response = client.get("/favicon.png")
    assert response.status_code == 200
