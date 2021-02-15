====================
 sphinxcontrib.nvd3
====================

Sphinx chart extension using NVD3.


Feature
=======
* provide some kinds of ``nvd3-`` prefixed directives to generate SVG chart from source.


Installation
============
Install with pip::

    $ pip install sphinxcontrib.nvd3


setup conf.py with::

    extensions = ["sphinxcontrib.nvd3"]

This package is NOT includes Javascript and CSS files (e.g. d3.js, nvd3.js and nvd3.css).

You need to add `setup` function into conf.py, as below::

    def setup(app):
        app.add_js_file("/path/to/d3.v3.js")
        app.add_js_file("/path/to/nv.d3.js")
        app.add_css_file("/path/to/nv.d3.css")

And then::

    $ make html


Requirement
===========
* python-nvd3 >= 0.13.10
* D3.js >= 3.0,<4.0
* Sphinx >= 3.0


License
=======

Licensed under the `Apache Software License <http://opensource.org/licenses/Apache-2.0>`_ .
See the LICENSE file for specific terms.


.. END
