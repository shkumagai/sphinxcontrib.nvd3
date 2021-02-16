# -*- coding: utf-8 -*-

from sphinxcontrib.nvd3 import directives


def setup(app):
    directives.setup(app)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
