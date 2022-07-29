"""Provide a web server to browse the examples."""
from pathlib import Path

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Mount
from starlette.routing import Route
from starlette.staticfiles import StaticFiles


HERE = Path(__file__).parent


def homepage(request: Request) -> HTMLResponse:
    """Handle the home page."""
    return HTMLResponse("<h1>Hello, world!</h1>")


routes = [
    Route("/", homepage),
    Mount("/examples", StaticFiles(directory=HERE / "examples")),
    Mount("/static", StaticFiles(directory=HERE / "static")),
]

app = Starlette(debug=True, routes=routes)
