from datetime import datetime
from typing import Dict, List

import ipyvuetify as v
import ipywidgets as ipw
import plotly.graph_objects as go
from plotly.subplots import make_subplots

v.theme.dark = True


def new_factory(news: List[Dict]) -> v.Html:
    children = []
    for new in news:
        date = datetime.fromtimestamp(new["providerPublishTime"])
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
                v.CardTitle(
                    children=[new["title"]],
                    style_="font-size: 1.1rem",
                ),
                v.CardSubtitle(
                    children=[
                        f'{new["publisher"]} ({date.strftime("%m/%d/%Y, %H:%M")})'
                    ]
                ),
                v.CardActions(children=[btn]),
            ],
        )
        children.append(card)
    return v.Html(tag="div", class_="d-flex flex-column", children=children)


def financial_info_factory(data: List[Dict], logo_url: str = None) -> v.Html:
    children = []
    if logo_url is not None:
        logo = v.Card(
            outlined=True,
            class_="ma-1",
            children=[v.Img(src=logo_url, height='100px', contain=True)],
            style_="width: calc(14.28% - 8px); min-width: 150px",
        )
        children.append(logo)
        
    for item in data:
        card = v.Card(
            outlined=True,
            class_="ma-1",
            children=[
                v.CardTitle(
                    primary_title=True,
                    children=[item["title"]],
                    style_="font-size: 18px; color: #51ef98",
                ),
                v.CardText(children=[str(item["value"])]),
            ],
            style_="width: calc(14.28% - 8px); min-width: 150px",
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
    widget = go.FigureWidget(fig, layout=ipw.Layout(height="100%"))
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


def text_widget(title: str, text: str) -> ipw.Widget:
    return v.Card(
        outlined=True,
        children=[
            v.CardTitle(
                children=[title],
                style_="font-size: 1.1rem",
            ),
            v.CardText(children=[text]),
        ],
    )
