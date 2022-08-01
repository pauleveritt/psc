"""Common settings and fixtures."""
import pytest
from starlette.testclient import TestClient

from psc import app

pytest_plugins = "psc.fixtures"


@pytest.fixture
def test_client() -> TestClient:
    """Return the app in a context manager to allow lifecyle to run."""
    with TestClient(app) as client:
        yield client
