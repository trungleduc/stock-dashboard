from distutils.command.config import config
from turtle import title
import ipyvuetify as v
from typing import Dict, List
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import ipywidgets as ipw

v.theme.dark = True


def new_factory(news: List[Dict]) -> v.Html:
    children = []
    for new in news:
        btn = v.Btn(
            small=True,
            text=True,
            block=True,
            children=["Open"],
            href=new["link"],
            target="_blank",
        )
        card = v.Card(
            outlined=True,
            children=[
                v.CardTitle(primary_title=True, children=[new["title"]]),
                v.CardSubtitle(children=[new["publisher"]]),
                v.CardActions(children=[btn]),
            ],
        )
        children.append(card)
    return v.Html(tag="div", class_="d-flex flex-column", children=children)


def financial_info_factory(data: List[Dict], ticker: str = "") -> v.Html:
    children = []
    for item in data:
        card = v.Card(
            outlined=True,
            class_="ma-1",
            children=[
                v.CardTitle(
                    primary_title=True,
                    children=[item["title"]],
                    style_="font-size: 1.1rem",
                ),
                v.CardText(children=[str(item["value"])]),
            ],
            style_="width: calc(16.6% - 8px); min-width: 150px",
        )
        children.append(card)
    return v.Html(
        tag="div", class_="d-flex flex-row", children=children, style_="flex-wrap: wrap"
    )


def price_chart_factory(df: List, ticker: str = "") -> ipw.Widget:
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # include candlestick with rangeselector
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="OHLC",
        ),
        secondary_y=True,
    )
    fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["Volume"],
            marker_color="rgba(91, 91, 91, 0.73)",
            name="Volume",
        ),
        secondary_y=False,
    )

    fig.layout.yaxis2.showgrid = False
    fig.update_layout(
        autosize=True,
        xaxis_rangeslider_visible=False,
        template="plotly_dark",
        title={
            "text": f"{ticker.upper()} PRICE CHART",
            "xanchor": "center",
            "yanchor": "top",
            "x": 0.5,
        },
    )
    widget = go.FigureWidget(fig, layout=ipw.Layout(height='100%'))
    return widget


def price_history_factory(df: List, ticker: str = "") -> ipw.Widget:
    # include candlestick with rangeselector
    widget = go.FigureWidget(go.Scatter(x=df.index, y=df["Close"]))
    widget.update_layout(
        autosize=True,
        template="plotly_dark",
        title={
            "text": f"{ticker.upper()} PRICE HISTORY",
            "xanchor": "center",
            "yanchor": "top",
            "x": 0.5,
        },
    )
    return widget
