"""Ensure the necessary static assets are in place."""
from bs4 import BeautifulSoup
from starlette.testclient import TestClient

from psc.app import app


def test_favicon() -> None:
    """Test the view for the favicon route."""
    client = TestClient(app)
    link_response = client.get("/index.html")
    soup = BeautifulSoup(link_response.text, "html5lib")
    link = soup.select_one('link[rel="icon"]')
    assert link
    favicon_href = link.get("href")
    assert favicon_href == "/favicon.png"
    favicon_response = client.get(favicon_href)
    assert favicon_response.status_code == 200


def test_bulma_css() -> None:
    """Test that Bulma is installed correctly."""
    client = TestClient(app)
    link_response = client.get("/index.html")
    soup = BeautifulSoup(link_response.text, "html5lib")
    link = soup.select_one('link[rel="stylesheet"]')
    assert link
    bulma_href = link.get("href")
    assert bulma_href == "/static/bulma.min.css"
    favicon_response = client.get(bulma_href)
    assert favicon_response.status_code == 200


def test_navbar_logo() -> None:
    """Test that the SVG logo is in static."""
    client = TestClient(app)
    link_response = client.get("/index.html")
    soup = BeautifulSoup(link_response.text, "html5lib")
    nav = soup.select_one("nav")
    assert nav
    logo = nav.select_one("img")
    assert logo
    logo_src = logo.get("src")
    assert logo_src == "/static/pyscript-sticker-black.svg"
    logo_response = client.get(logo_src)
    assert logo_response.status_code == 200
