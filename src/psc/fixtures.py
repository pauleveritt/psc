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
    is_asm = "asm" in route.request.url
    if is_asm:
        with open("/tmp/foo.txt", "w") as f:
            f.write("111")
    content_type = "application/wasm"
    if is_fake:
        # We should read something from the filesystem
        # if this_path.endswith(".html") or this_path.endswith(".css"):
        this_fs_path = HERE / this_path
        if this_fs_path.exists():
            with open(this_fs_path, 'rb') as f:
                body = f.read()
            if this_path.endswith(".asm.wasm"):
                content_type = "application/wasm"
            if this_path.endswith(".js"):
                content_type = "application/javascript"
            elif this_path.endswith(".html"):
                content_type = "text/html"
            elif this_path.endswith(".css"):
                content_type = "text/css"
            elif this_path.endswith(".png"):
                content_type = "image/png"
            elif this_path.endswith(".tar"):
                print("\n\n#### TAR")
                content_type = "application/x-tar"
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
        headers={"content-type": content_type}
    )


@pytest.fixture
def fake_page(page: Page) -> Page:  # pragma: no cover
    """On the fake server, intercept and return from fs."""

    def _route_handler(route: Route) -> None:
        """Instead of doing this inline, call to a helper for easier testing."""
        route_handler(page, route)


    # Use Playwright's route method to intercept any URLs pointed at the
    # fake server and run through the interceptor instead.
    page.route("**", _route_handler)
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    return page
