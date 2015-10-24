.. This is index.rst of document.

.. include:: ../README.rst

.. include:: ../AUTHORS.rst

.. include:: ../CHANGES.rst


Sample Charts
=============

.. toctree::
   :maxdepth: 1

   charts/line
   charts/lineplusbar
   charts/linewithfocus
   charts/cumulativeline
   charts/discretebar
   charts/multibar
   charts/multibarhorizontal
   charts/pie
   charts/scatter
   charts/stackedarea


Options
=======

The following keywords from python-nvd3 are acceptable.
Please refer to nvd3docs_ for details:

- jquery_on_ready
- charttooltip_dateformat
- name
- color_category
- color_list
- margin_top
- margin_right
- margin_bottom
- margin_left
- width
- height
- stacked
- resize
- show_legend
- show_labels
- tag_script_js
- use_interactive_guideline
- chart_attr
- chart_kwargs
- extras
- x_is_date
- x_axis_format
- style


Additionaly, following keywords are acceptable:

:encoding:
   specify a character encoding for input file. default value depends on 'source_encoding'.

:delimiter:
   specify a line delimiter for input file. ',' as default.

:window_onload:
   enable to execute js codes for chart on 'onload' event


.. _nvd3docs: http://python-nvd3.readthedocs.org/en/latest/classes-doc/NVD3Chart.html
