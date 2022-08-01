"""Test the Starlette web app for browsing pages."""
from bs4 import BeautifulSoup
from starlette.testclient import TestClient

from psc.app import app


def test_homepage(test_client: TestClient) -> None:
    """Test the view for the index route."""
    response = test_client.get("/")
    assert response.status_code == 200
    soup = BeautifulSoup(response.text, "html5lib")
    title = soup.select_one("title")
    assert title
    assert title.text == "Home Page | PyScript Collective"
    main = soup.select_one("main")
    assert main
