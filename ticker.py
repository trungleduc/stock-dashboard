from typing import Dict, List
import yfinance as yf
from pathlib import Path
import os, time, json


class TickerData:
    def __init__(self, ticker: str) -> None:
        ticker = ticker.upper()
        self.fetch_ticker(ticker)

    def fetch_ticker(self, ticker: str):
        self._ticker = yf.Ticker(ticker)
        cache = f'./cache/{ticker}.json'
        cached = os.path.exists(cache)
        if not cached:
            os.makedirs(os.path.dirname(cache), exist_ok=True)
            time_delta = 100
        else:
            time_delta = (time.time() - os.path.getmtime(cache)) / (
                60 * 60 * 24
            )

        if not cached or time_delta > 1:
            self._info = self._ticker.get_info()
            self.news = self._ticker.news
            with open(cache, 'w') as f:
                json.dump({'info': self._info, 'news': self.news}, f)
        else:
            with open(cache, 'r') as f:
                cached_data = json.load(f)
                self._info = cached_data['info']
                self.news = cached_data['news']

    @property
    def financial_info(self) -> List[Dict]:
        data = [
            {'title': 'Market cap', 'value': self._info['marketCap']},
            {'title': 'PE Ratio', 'value': self._info['forwardPE']},
            {'title': 'Total revenue', 'value': self._info['totalRevenue']},
            {'title': 'Gross profit', 'value': self._info['grossProfits']},
            {'title': 'Debt to equity', 'value': self._info['debtToEquity']},
            {'title': 'Profit margin', 'value': self._info['profitMargins']},
        ]
        return data

    def price(self, history='6mo') -> List:
        return self._ticker.history(history)

    @property
    def balance_sheet(self):
        return self._ticker.balance_sheet

    @property
    def analysis(self):
        return self._ticker.analysis.transpose()
