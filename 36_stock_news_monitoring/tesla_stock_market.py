import requests
import os
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


STOCK_API_KEY = "MKEIPQHOCRCM2R51"
NEWS_API_KEY = "2f5a4be952424eb58265a4179d870d7d"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

TW_SID = "ACee3ed3f3c6abfba811307def53f778ce"
TW_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
if stock_response.status_code == 200:
    data = stock_response.json()
    daily_time_series = data["Time Series (Daily)"]

    everyday_stocks = [k for (k, v) in daily_time_series.items()]

    yesterday_close_price_k = daily_time_series[everyday_stocks[0]]  # if we put k in the dict comprehension

    # yesterday_close_price_v = everyday_stocks[0]  # if we put v in front as variable

    day_before_yesterday_close_price = daily_time_series[everyday_stocks[1]]

    ycp = float(yesterday_close_price_k["4. close"])
    dbycp = float(day_before_yesterday_close_price["4. close"])
    diff = ycp - dbycp

    up_down = None
    if diff > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    percentage_difference = (diff / dbycp) * 100
    percentage_difference = abs(round(percentage_difference))

    if percentage_difference > 3:
        news_param = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": COMPANY_NAME,  # most of time articles are using company names instead of company stock names
        }
        news_response = requests.get(NEWS_ENDPOINT, params=news_param)
        news_response.raise_for_status()
        if news_response.status_code == 200:
            articles = news_response.json()["articles"]
            three_articles = articles[:3]

            formatted_articles = [
                f"{STOCK_NAME}: {up_down}{diff}%\nHeadline: {article['title']}. Brief: {article['description']}" for article in three_articles
            ]

            client = Client(TW_SID, TW_AUTH_TOKEN)
            for article in formatted_articles:
                message = client.messages.create(
                    body=article,
                    from_="+18302665362",
                    to="+35989_878_4412"
                )

