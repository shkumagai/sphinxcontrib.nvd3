====================
 sphinxcontrib.nvd3
====================

Cumulative Line Chart
=====================

.. nvd3-cumulativelinechart:: cumulativeline-sample.csv
   :x_is_date:


Discrete Bar Chart
==================

.. nvd3-discretebarchart:: discretebar-sample.csv


Line Chart
==========

.. nvd3-linechart:: line-sample.csv
   :use_interactive_guideline:
   :x_is_date:
   :x_axis_format: AM_PM
   :extras: {"tooltip": {"y_start": "", "y_end": ""}}


Line Plus Bar Chart
===================

.. nvd3-lineplusbarchart:: line-sample.csv
   :chart_kwargs: {"ydata1": {"bar": true}}


Line With Focus Chart
=====================

.. nvd3-linewithfocuschart:: line-sample.csv


Multi Bar Chart
===============

.. nvd3-multibarchart:: multibar-sample.csv


Multi Bar Horizontal Chart
==========================

.. nvd3-multibarhorizontalchart:: multibar-sample.csv


Pie Chart
=========

.. nvd3-piechart:: pie-sample.csv


Scatter Chart
=============

.. nvd3-scatterchart:: scatter-sample.csv
   :height: 350
   :extras: {"tooltip": {"y_start": "", "y_end": " calls"}}


Stacked Area Chart
==================

.. nvd3-stackedareachart:: stackedarea-sample.csv


.. END
