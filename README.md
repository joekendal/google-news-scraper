### Description
Tool for grabbing current stock headlines from Google News. Useful for collecting real-time data on a periodic basis.

### Usage
```python
from gn_scraper import GoogleNews

gn = GoogleNews()

symbol = "GOOGL"

gn.fetch_news(symbol)
```