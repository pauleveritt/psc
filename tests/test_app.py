"""Test the Starlette web app for browsing examples."""
import pytest
from playwright.sync_api import Page
from starlette.testclient import TestClient

from psc.app import app


def test_homepage() -> None:
    """Test the view for the index route."""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200


def test_first_example() -> None:
    """Test the static HTML for examples/first.html."""
    client = TestClient(app)
    response = client.get("/examples/first.html")
    assert response.status_code == 200
    assert "<title>First" in response.text


@pytest.mark.full
def test_first_example_full(fake_page: Page) -> None:
    """Use Playwright to do a test on the first example."""
    fake_page.goto("http://fake/examples/first.html")
    assert fake_page.title() == "First Example"
