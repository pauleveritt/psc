"""pytest fixtures to make testing easier."""
from urllib.parse import urlparse

import pytest
from playwright.sync_api import Page
from playwright.sync_api import Route

from psc.app import HERE


def route_handler(page: Page, route: Route) -> None:
    """Handle fake requests."""
    # Add a prefix to the title.
    this_url = urlparse(route.request.url)
    this_path = this_url.path[1:]
    is_fake = this_url.hostname == "fake"
    if is_fake:
        # We should read something from the filesystem
        # if this_path.endswith(".html") or this_path.endswith(".css"):
        this_fs_path = HERE / this_path
        if this_fs_path.exists():
            with open(this_fs_path) as f:
                body = f.read()
        else:
            raise ValueError("That path doesn't exist on disk.")
    else:
        # This is to a non-fake server. In theory, we shouldn't get
        # here, as page.route below says to only cover requests to
        # http://fake/. So this is a "just in case" it's misconfigured.
        response = page.request.fetch(route.request)
        body = response.text()
    route.fulfill(
        body=body,
    )


@pytest.fixture
def fake_page(page: Page) -> Page:  # pragma: no cover
    """On the fake server, intercept and return from fs."""

    def _route_handler(route: Route) -> None:
        """Instead of doing this inline, call to a helper for easier testing."""
        return route_handler(page, route)

    # Use Playwright's route method to intercept any URLs pointed at the
    # fake server and run through the interceptor instead.
    page.route("http://fake/**", _route_handler)
    return page
