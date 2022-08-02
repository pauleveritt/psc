"""Ensure the necessary static assets are in place."""
from starlette.testclient import TestClient

from psc.fixtures import SoupGetter


def test_favicon(get_soup: SoupGetter, test_client: TestClient) -> None:
    """Test the view for the favicon route."""
    soup = get_soup("/index.html")
    link = soup.select_one('link[rel="icon"]')
    assert link
    favicon_href = link.get("href")
    assert favicon_href == "/favicon.png"
    favicon_response = test_client.get(favicon_href)
    assert favicon_response.status_code == 200


def test_screenshot(test_client: TestClient) -> None:
    """Examples have screenshots which need a special route."""
    response = test_client.get("/gallery/hello_world/screenshot.png")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"


def test_bulma_css(get_soup: SoupGetter, test_client: TestClient) -> None:
    """Test that Bulma is installed correctly."""
    soup = get_soup("/index.html")
    link = soup.select('link[rel="stylesheet"]')[1]
    assert link
    bulma_href = link.get("href")
    assert bulma_href == "/static/bulma.min.css"
    favicon_response = test_client.get(bulma_href)
    assert favicon_response.status_code == 200


def test_navbar_logo(get_soup: SoupGetter, test_client: TestClient) -> None:
    """Test that the SVG logo is in static."""
    soup = get_soup("/index.html")
    nav = soup.select_one("nav")
    assert nav
    logo = nav.select_one("img")
    assert logo
    logo_src = logo.get("src")
    assert logo_src == "/static/pyscript-sticker-black.svg"
    logo_response = test_client.get(logo_src)
    assert logo_response.status_code == 200
