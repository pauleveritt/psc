"""Ensure our pytest fixtures work correctly."""
from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import cast

import pytest
from playwright.sync_api import Page
from playwright.sync_api import Route

from psc.fixtures import route_handler


def test_route_handler_fake_bad_path() -> None:
    """Fake points at bad path in ``examples``."""
    dummy_request = DummyRequest(url="https://fake/staticxx")
    dummy_page = DummyPage(request=dummy_request)
    dummy_route = DummyRoute(request=dummy_request)
    with pytest.raises(ValueError) as exc:
        route_handler(
            cast(Page, dummy_page),
            cast(Route, dummy_route),
        )
    assert str(exc.value) == "That path doesn't exist on disk."


def test_route_handler_fake_good_path() -> None:
    """Fake points at good path in ``examples``."""
    dummy_request = DummyRequest(url="https://fake/static/psc.css")
    dummy_page = DummyPage(request=dummy_request)
    dummy_route = DummyRoute(request=dummy_request)
    route_handler(
        cast(Page, dummy_page),
        cast(Route, dummy_route),
    )
    if dummy_route.body:
        body = str(dummy_route.body)
        assert body.startswith("b'body {")


def test_route_handler_non_fake() -> None:
    """Not using a fake, simulate a network request."""
    dummy_request = DummyRequest(url="https://good/static/psc.css")
    dummy_page = DummyPage(request=dummy_request)
    dummy_route = DummyRoute(request=dummy_request)
    route_handler(
        cast(Page, dummy_page),
        cast(Route, dummy_route),
    )
    assert dummy_route.body == "URL Returned Text"


@dataclass
class DummyResponse:
    """Fake the Playwright ``Response`` class."""

    dummy_text: str = ""
    headers: dict[str, object] = field(
        default_factory=lambda: {"Content-Type": "text/html"}
    )

    def text(self) -> str:
        """Fake the text method."""
        return self.dummy_text


@dataclass
class DummyRequest:
    """Fake the Playwright ``Request`` class."""

    url: str

    @staticmethod
    def fetch(request: DummyRequest) -> DummyResponse:
        """Fake the fetch method."""
        return DummyResponse(dummy_text="URL Returned Text")


@dataclass
class DummyRoute:
    """Fake the Playwright ``Route`` class."""

    request: DummyRequest
    body: str | None = None
    headers: dict[str, object] | None = None

    def fulfill(self, body: str, headers: dict[str, object]) -> None:
        """Stub the Playwright ``route.fulfill`` method."""
        self.body = body
        self.headers = headers


@dataclass
class DummyPage:
    """Fake the Playwright ``Page`` class."""

    request: DummyRequest
