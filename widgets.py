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
            href=new['link'],
            target="_blank"
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
