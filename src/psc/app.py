"""Provide a web server to browse the examples."""
from pathlib import PurePath

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import FileResponse
from starlette.routing import Mount
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

from psc.here import HERE
from psc.resources import Example


templates = Jinja2Templates(directory=HERE / "templates")


async def favicon(request: Request) -> FileResponse:
    """Handle the favicon."""
    return FileResponse(HERE / "favicon.png")


async def homepage(request: Request) -> _TemplateResponse:
    """Handle the home page."""
    index_file = HERE / "index.html"

    return templates.TemplateResponse(
        "page.jinja2",
        dict(
            title="Home Page",
            main=index_file.read_text(),
            request=request,
        ),
    )


async def example(request: Request) -> _TemplateResponse:
    """Handle an example page."""
    example_path = PurePath(request.path_params["example_name"])
    example = Example(path=example_path)

    return templates.TemplateResponse(
        "example.jinja2",
        dict(
            title=example.title,
            extra_head=example.extra_head,
            main=example.main,
            extra_pyscript=example.extra_pyscript,
            request=request,
        ),
    )


routes = [
    Route("/", homepage),
    Route("/index.html", homepage),
    Route("/examples/{example_name}/index.html", example),
    Route("/favicon.png", favicon),
    Mount("/examples", StaticFiles(directory=HERE / "examples")),
    Mount("/static", StaticFiles(directory=HERE / "static")),
]

app = Starlette(debug=True, routes=routes)
