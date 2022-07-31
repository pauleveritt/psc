"""Test the Starlette web app for browsing pages."""
from bs4 import BeautifulSoup
from starlette.testclient import TestClient

from psc.app import app


def test_homepage() -> None:
    """Test the view for the index route."""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    soup = BeautifulSoup(response.text, "html5lib")
    main = soup.select_one("main")
    assert main
