#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- General configuration ------------------------------------------------

source_suffix = ".rst"

master_doc = "index"

# General information about the project.
project = "sphinxcontrib.nvd3"

copyright = "2015-2021, Shoji KUMAGAI"

author = "Shoji KUMAGAI"

version = "0.2.2"
release = "0.2.2"

extensions = ["sphinxcontrib.nvd3"]

language = None


# -- Options for HTML output ----------------------------------------------

pygments_style = "sphinx"

html_theme = "bizstyle"

html_static_path = ["_static"]


def setup(app):
    app.add_js_file("https://nvd3.org/assets/lib/d3.v3.js")
    app.add_js_file("https://nvd3.org/assets/js/nv.d3.js")
    app.add_css_file("https://nvd3.org/assets/css/nv.d3.css")
