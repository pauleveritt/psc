"""Test the ``Hello World`` example."""
import pytest
from playwright.sync_api import Page

from psc.fixtures import SoupGetter


def test_hello_world(get_soup: SoupGetter) -> None:
    """Test the static HTML for Hello World."""
    soup = get_soup("/gallery/examples/hello_world/index.html")

    # Title and subtitle
    title = soup.select_one("title")
    assert title
    assert title.text == "Hello World | PyScript Collective"
    subtitle = soup.select_one('meta[name="subtitle"]')
    assert subtitle
    assert (
        subtitle.get("content")
        == "The classic hello world, but in Python -- in a browser!"
    )

    # See if extra_head got filled, then resolve those
    assert soup.find_all("link", href="hello_world.css")
    assert soup.find_all("script", src="hello_world.js")

    # Ensure the ``<main>`` got filled
    assert soup.select_one("main")

    # Only one <py-config>, pointing to local runtime
    py_configs = soup.select("py-config")
    assert len(py_configs) == 1

    # The <py-script> is present
    py_scripts = soup.select("py-script")
    assert len(py_scripts) == 1

    # The tracer <h6> is not present
    assert not soup.select("h6")


@pytest.mark.full
def test_hello_world_full(fake_page: Page) -> None:
    """Use Playwright to do a test on Hello World."""
    url = "http://fake/gallery/examples/hello_world/index.html"
    fake_page.goto(url)
    # Turn this on when using `PWDEBUG=1` to run "head-ful"
    fake_page.pause()
    element = fake_page.wait_for_selector("text=...world")
    if element:
        assert element.text_content() == "...world"
