#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- General configuration ------------------------------------------------

source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = 'sphinxcontrib.nvd3'

copyright = '2015, Shoji KUMAGAI'

author = 'Shoji KUMAGAI'

version = '0.1.4'
release = '0.1.4'

extensions = ['sphinxcontrib.nvd3']

language = None


# -- Options for HTML output ----------------------------------------------

pygments_style = 'sphinx'

html_theme = 'bizstyle'

html_static_path = ['_static']


def setup(app):
    app.add_javascript("http://nvd3.org/assets/lib/d3.v3.js")
    app.add_javascript("http://nvd3.org/assets/js/nv.d3.js")
    app.add_stylesheet("http://nvd3.org/assets/css/nv.d3.css")
