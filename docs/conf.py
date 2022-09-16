# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from pathlib import Path

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath("."))

from preprocessing import run_all  # noqa

run_all(["IVT", "IVT_evening"])

# -- Project information -----------------------------------------------------

project = "MEPhI Docs"
copyright = "2022, 0dminnimda"
author = "0dminnimda"


# -- General configuration ---------------------------------------------------

language = "ru"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinxcontrib.mermaid",
    # "mathjax",
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

mermaid_init_js = (
    "mermaid.initialize({startOnLoad:true, flowchart: {useMaxWidth:false}});"
)

# latex_elements = {
#     "preamble": r"\input{preamble.sty}",
#     # "preamble": Path("preamble.sty").read_text(),
# }

# latex_additional_files = ["preamble.sty"]

# mathjax3_config = {
#     "TeX": {
#         "Macros": {
#             "braket": ["\\langle #1 \\rangle", 1],
#             "wrapmat": ["\\begin{#1} #2 \\end{#1}", 2],
#             "mat": ["\\wrapmat{Vmatrix}{#1}", 1],
#             "det": ["\\wrapmat{vmatrix}{#1}", 1],
#             "upline": ["\\overline{#1}", 1],
#             "dnline": ["\\underline{#1}", 1],
#         }
#     }
# }

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

html_logo = "_static/images/logo_mifi.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# html_css_files = [
#     # "/stylesheets/extra.css",
#     # "/mobile-viewer/viewer.css",
# ]


# html_js_files = [
# ]
