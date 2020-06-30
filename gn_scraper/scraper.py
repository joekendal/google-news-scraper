from typing import Dict, List
import feedparser
import time
import json


class GoogleNews:
    """"
    GoogleNews is the main scraper object

    Methods
    -------
    fetch_news(ticker)
        Fetches the current headlines
    """

    @staticmethod
    def __parse_news(articles: List, ticker: str) -> List[Dict[str, str]]:
        """
        Formats results for InfluxDB

        Parameters
        ----------
        articles : list
            The JSON result data
        ticker : str
            The ticker symbol
        """
        for x, article in enumerate(articles):
            # InfluxDB scheme
            articles[x]: Dict[str, str] = {
                "measurement": "news_article",
                "tags": {
                    "ticker": ticker,
                },
                "time": time.strftime('%Y-%m-%dT%H:%M:%SZ', article.published_parsed),
                "fields": {
                    "title": article.title,
                    "url": article.link,
                },
            }
        return articles

    def fetch_news(self, ticker: str) -> List[Dict[str, str]]:
        """
        Fetches the current Google News results

        Parameters
        ----------
        ticker : str
            The stock ticker symbol
        """
        url = f'https://news.google.com/rss/search?q={ticker}'

        data = feedparser.parse(url)

        return self.__parse_news(data.entries, ticker)
