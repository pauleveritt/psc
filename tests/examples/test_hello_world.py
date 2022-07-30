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
    assert "<title>PyScript Hello World" in response.text


@pytest.mark.full
def test_hello_world_full(fake_page: Page) -> None:
    """Use Playwright to do a test on Hello World."""
    # url = "http://127.0.0.1:3000/examples/hello_world/index.html"
    url = "http://fake/examples/hello_world/index.html"
    fake_page.goto(url)
    element = fake_page.wait_for_selector("text=...world")
    # Turn this on when using `PWDEBUG=1` to run "head-ful"
    # fake_page.pause()
    assert element.text_content() == "...world"
