"""Provide a web server to browse the examples."""
from pathlib import Path

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import FileResponse
from starlette.routing import Mount
from starlette.routing import Route
from starlette.staticfiles import StaticFiles

HERE = Path(__file__).parent


async def favicon(request: Request) -> FileResponse:
    return FileResponse(HERE / "favicon.png")


async def homepage(request: Request) -> FileResponse:
    """Handle the home page."""
    return FileResponse(HERE / "index.html")


routes = [
    Route("/", homepage),
    Route("/index.html", homepage),
    Route("/favicon.png", favicon),
    Mount("/examples", StaticFiles(directory=HERE / "examples")),
    Mount("/static", StaticFiles(directory=HERE / "static")),
]

app = Starlette(debug=True, routes=routes)
