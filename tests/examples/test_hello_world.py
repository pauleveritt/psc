"""Test the ``Hello World`` example."""
import pytest
from playwright.sync_api import Page
from starlette.testclient import TestClient

from psc.app import app


def test_hello_world() -> None:
    """Test the static HTML for Hello World."""
    client = TestClient(app)
    response = client.get("/examples/hello_world/index.html")
    assert response.status_code == 200
    assert "<title>First" in response.text


@pytest.mark.full
def test_hello_world_full(fake_page: Page) -> None:
    """Use Playwright to do a test on Hello World."""
    fake_page.goto("http://fake/examples/hello_world/index.html")
    assert fake_page.title() == "First Example"
