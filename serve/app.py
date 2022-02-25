from typing import Callable
from flask import Flask, render_template

import examples

app = Flask(__name__)
from pydacharts.models import Config

from examples.bar import floating_bar, horizontal_bar, rounded_bar, stacked_bar, vertical_bar  # noqa
from examples.line import line, multi_axis, stepped_line, styled_line  # noqa: F401
from examples.pie import pie  # noqa: F401
from examples.other import sankey  # noqa: F401
from examples.datalabels import datalabels  # noqa: F401


@app.route("/")
def hello_world():

    chart_types = dict(
        floating_bar=floating_bar,
        horizontal_bar=horizontal_bar,
        rounded_bar=rounded_bar,
        stacked_bar=stacked_bar,
        vertical_bar=vertical_bar,
        line=line,
        multi_axis=multi_axis,
        stepped_line=stepped_line,
        styled_line=styled_line,
        pie=pie,
        sankey=sankey,
        datalabels=datalabels
    )

    config = examples.datalabels  # type: Callable[[], Config]
    config_json = config().json(exclude_none=True, indent=2)
    return render_template(
        "index.html",
        charts = {k: v().json(exclude_none=True, indent=2) for k, v in chart_types.items()}
    )



@app.route("/example/datalabels")
def get_datalabels_chart():
    config = examples.datalabels  # type: Callable[[], Config]
    config_json = config().json(exclude_none=True, indent=2)
    return render_template(
        "chart_datalabels.html",
        config=config_json,
    )


@app.route("/example/<name>")
def get_chart(name):
    config = getattr(examples, name)()  # type: Config
    config_json = config.json(exclude_none=True, indent=2)
    return render_template(
        "chart.html",
        config=config_json,
    )
