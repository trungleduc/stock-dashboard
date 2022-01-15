from typing import Dict, List
import yfinance as yf

class TickerData:
  def __init__(self, ticker: str) -> None:
      self._ticker = yf.Ticker(ticker)
      self._info = self._ticker.get_info()
      
  @property
  def news(self)-> List:
    return self._ticker.news

  @property
  def financial_info(self)-> List[Dict]:
    data = [
      {"title": "Market cap", "value": self._info['marketCap']},
      {"title": "PE Ratio", "value": self._info['forwardPE']},
      {"title": "Total revenue", "value": self._info['totalRevenue']},
      {"title": "Gross profit", "value": self._info['grossProfits']},
      {"title": "Debt to equity", "value": self._info['debtToEquity']},
      {"title": "Profit margin", "value": self._info['profitMargins']},
    ]
    return data