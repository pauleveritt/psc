"""Test the Starlette web app for browsing pages."""

from psc.fixtures import SoupGetter


def test_homepage(get_soup: SoupGetter) -> None:
    """Test the view for the index route."""
    # response = test_client.get("/")
    # assert response.status_code == 200
    soup = get_soup("/")

    # Title and main
    title = soup.select_one("title")
    assert title
    assert title.text == "Home Page | PyScript Collective"
    section = soup.select_one("section")
    assert section


def test_examples_listing(get_soup: SoupGetter) -> None:
    """Ensure the route lists the examples."""
    # First get the URL from the navbar.
    index_soup = get_soup("/")
    nav_examples = index_soup.select_one("#navbarGallery")
    assert nav_examples
    examples_href = nav_examples.get("href")
    assert examples_href
    examples_soup = get_soup(examples_href)
    assert examples_soup

    # Example title
    examples_title = examples_soup.select_one("title")
    assert examples_title
    assert examples_title.text == "Gallery | PyScript Collective"

    # Example subtitle
    subtitle = examples_soup.select_one("p.subtitle")
    assert subtitle
    assert "Curated" in subtitle.text

    # Example description
    description_em = examples_soup.select_one("div.content em")
    assert description_em
    assert description_em.text == "hello world"

    # Get the first example, follow the link, ensure it is Hello World
    first_example = examples_soup.select_one("p.title a")
    assert first_example
    first_href = first_example.get("href")
    assert first_href == "/gallery/examples/hello_world"
    hello_soup = get_soup(first_href)
    assert hello_soup
    title = hello_soup.select_one("title")
    assert title
    assert title.text == "Hello World | PyScript Collective"
