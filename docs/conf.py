"""Sphinx configuration."""
project = "PyScript Collective"
author = "Paul Everitt"
copyright = "2022, Paul Everitt"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
