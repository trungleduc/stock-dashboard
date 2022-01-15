import ipyvuetify as v
from typing import Dict, List


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


def financial_info_factory(data: List[Dict]) -> v.Html:
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
            style_="width: calc(16.667% - 8px)",
        )
        children.append(card)
    return v.Html(tag="div", class_="d-flex flex-row", children=children)
