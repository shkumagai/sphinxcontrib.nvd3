# -*- coding: utf-8 -*-

import codecs
import json
import re
import sys

from docutils import nodes
from docutils.parsers import rst
from nvd3 import (
    cumulativeLineChart,
    discreteBarChart,
    lineChart,
    linePlusBarChart,
    lineWithFocusChart,
    multiBarChart,
    multiBarHorizontalChart,
    pieChart,
    scatterChart,
    stackedAreaChart,
)
from sphinx.directives.code import dedent_lines


def nonnegative_int_list(argument):
    if "," in argument:
        entries = argument.split(",")
    else:
        entries = argument.split()
    return [rst.directives.nonnegative_int(entry) for entry in entries]


def string_list(argument):
    if "," in argument:
        entries = argument.split(",")
    else:
        entries = argument.split()
    return [rst.directives.hoge(entry) for entry in entries]


class nvd3_node(nodes.FixedTextElement):
    pass


class NVD3DirectiveBase(rst.Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "jquery_on_ready": rst.directives.flag,
        "window_onload": rst.directives.flag,
        "charttooltip_dateformat": rst.directives.unchanged,
        "name": rst.directives.unchanged,
        "color_category": rst.directives.unchanged,
        "color_list": string_list,
        "margin_top": int,
        "margin_right": int,
        "margin_bottom": int,
        "margin_left": int,
        "width": rst.directives.nonnegative_int,
        "height": rst.directives.nonnegative_int,
        "stacked": rst.directives.flag,
        "resize": rst.directives.flag,
        "show_legend": rst.directives.flag,
        "show_labels": rst.directives.flag,
        "tag_script_js": rst.directives.flag,
        "use_interactive_guideline": rst.directives.flag,
        "chart_attr": rst.directives.unchanged,
        "chart_kwargs": rst.directives.unchanged,
        "extras": rst.directives.unchanged,
        "x_is_date": rst.directives.flag,
        "x_axis_format": rst.directives.unchanged,
        "style": rst.directives.unchanged,
        "encoding": rst.directives.encoding,
        "delimiter": rst.directives.single_char_or_whitespace_or_unicode,
    }

    def read_with_encoding(self, filename, document, codec_info, encoding):
        f = None
        try:
            f = codecs.StreamReaderWriter(
                open(filename, "rb"), codec_info[2], codec_info[3], "strict"
            )
            lines = f.readlines()
            lines = dedent_lines(lines, self.options.get("dedent"))
            return lines

        except (IOError, OSError):
            return [
                document.reporter.warning(
                    "Include file %r not found or reading it failed" % filename,
                    line=self.lineno,
                )
            ]

        except UnicodeError:
            return [
                document.reporter.warning(
                    "Encoding %r used for reading included file %r seems to"
                    "be wrong, try giving an :encoding: option" % (encoding, filename)
                )
            ]

        finally:
            if f is not None:
                f.close()

    def _parse(self, value):
        try:
            return float(value) if "." in value else int(value)
        except ValueError:
            return value

    def replace_function_prefix(self, text):
        return re.sub(r"\$\(function", "(window.onload = function", text)

    def __get_lines(self):
        if self.arguments:
            document = self.state.document

            if self.content:
                sys.stdout.write("have both content and filename.\n")
                msg = (
                    "%s directive cannot have both content and "
                    "a filename argument" % self.name
                )
                return [document.reporter.warning(msg, line=self.lineno)]

            env = document.settings.env
            rel_filename, filename = env.relfn2path(self.arguments[0])
            encoding = self.options.get("encoding", env.config.source_encoding)
            codec_info = codecs.lookup(encoding)

            lines = self.read_with_encoding(filename, document, codec_info, encoding)

        else:
            content = "\n".join(self.content).strip()
            if not content:
                msg = ('Ignoring "%s" directive without content.' % self.name,)
                return [self.state_machine.reporter.warning(msg, line=self.lineno)]

            lines = content.split("\n")
        return lines

    def run(self):
        lines = self.__get_lines()
        if lines and not isinstance(lines[0], (bytes, str)):
            return lines

        self.delimiter = self.options.get("delimiter", ",")

        data_keys = lines[0].strip().split(self.delimiter)

        self.dataset = {
            "xdata": [],
            "ydata": [[] for n in range(len(data_keys) - 1)],
        }

        for line in lines[1:]:
            values = line.strip().split(self.delimiter)
            for pos in range(len(values)):
                if pos == 0:
                    self.dataset["xdata"].append(self._parse(values[pos]))
                else:
                    self.dataset["ydata"][pos - 1].append(self._parse(values[pos]))

        self.dataset["data_keys"] = data_keys[1:]

        self.options["jquery_on_ready"] = (
            "window_onload" in self.options or "jquery_on_ready" in self.options
        )

        self.options["stacked"] = "stacked" in self.options
        # self.options['focus_enable'] = 'focus_enable' in self.options
        self.options["resize"] = "resize" in self.options
        self.options["show_legend"] = "show_legend" not in self.options
        self.options["show_labels"] = "show_labels" not in self.options
        self.options["tag_script_js"] = "tag_script_js" not in self.options

        self.options["x_is_date"] = "x_is_date" in self.options

        self.options["use_interactive_guideline"] = (
            "use_interactive_guideline" in self.options
        )

        if "chart_attr" in self.options:
            self.options["chart_attr"] = json.loads(
                self.options.get("chart_attr", "{}"),  # noqa: P103
            )

        self.chart_kwargs = json.loads(
            self.options.get("chart_kwargs", "{}"),  # noqa: P103
        )
        self.extra_serie = json.loads(
            self.options.get(
                "extras",
                '{"tooltip": {"y_start": "", "y_end": ""} }',
            ),
        )

        # construct chart content
        length = len(self.dataset["ydata"])
        chart = self.klass(**self.options)

        for index in range(length):
            kwargs = self.chart_kwargs.get(self.dataset["data_keys"][index], {})

            chart.add_serie(
                y=self.dataset["ydata"][index],
                x=self.dataset["xdata"],
                name=self.dataset["data_keys"][index],
                extra=self.extra_serie,
                **kwargs,
            )

        chart.buildcontent()

        attributes = {}
        text = chart.htmlcontent
        if "window_onload" in self.options:
            text = self.replace_function_prefix(text)
        raw_node = nvd3_node("", text, **attributes)

        (raw_node.source, raw_node.line) = self.state_machine.get_source_and_line(
            self.lineno
        )

        return [raw_node]


class CumulativeLineChartDirective(NVD3DirectiveBase):
    klass = cumulativeLineChart


class DiscreteBarChartDirective(NVD3DirectiveBase):
    klass = discreteBarChart


class LineChartDirective(NVD3DirectiveBase):
    klass = lineChart


class LinePlusBarChartDirective(NVD3DirectiveBase):
    klass = linePlusBarChart


class LineWithFocusChartDirective(NVD3DirectiveBase):
    klass = lineWithFocusChart


class MultiBarChartDirective(NVD3DirectiveBase):
    klass = multiBarChart


class MultiBarHorizontalChartDirective(NVD3DirectiveBase):
    klass = multiBarHorizontalChart


class PieChartDirective(NVD3DirectiveBase):
    klass = pieChart


class ScatterChartDirective(NVD3DirectiveBase):
    klass = scatterChart


class StackedAreaChartDirective(NVD3DirectiveBase):
    klass = stackedAreaChart


def visit_nvd3_node(self, node):
    self.body.append(self.starttag(node, "div"))
    self.body.append(node.astext())
    self.body.append("</div>")
    raise nodes.SkipNode


def depart_nvd3_node(self, node=None):
    pass


def setup(app):
    app.add_node(nvd3_node, html=(visit_nvd3_node, depart_nvd3_node))

    rst.directives.register_directive(
        "nvd3-cumulativelinechart", CumulativeLineChartDirective
    )
    rst.directives.register_directive(
        "nvd3-discretebarchart", DiscreteBarChartDirective
    )
    rst.directives.register_directive("nvd3-linechart", LineChartDirective)
    rst.directives.register_directive(
        "nvd3-lineplusbarchart", LinePlusBarChartDirective
    )
    rst.directives.register_directive(
        "nvd3-linewithfocuschart", LineWithFocusChartDirective
    )
    rst.directives.register_directive("nvd3-multibarchart", MultiBarChartDirective)
    rst.directives.register_directive(
        "nvd3-multibarhorizontalchart", MultiBarHorizontalChartDirective
    )
    rst.directives.register_directive("nvd3-piechart", PieChartDirective)
    rst.directives.register_directive("nvd3-scatterchart", ScatterChartDirective)
    rst.directives.register_directive(
        "nvd3-stackedareachart", StackedAreaChartDirective
    )
