# Stock Trading News Alert Project - Monitors Tesla stock price and sends news alerts on significant changes
import requests
from twilio.rest import Client

# Twilio configuration
VIRTUAL_TWILIO_NUMBER = "YOUR VIRTUAL TWILIO NUMBER"
VERIFIED_NUMBER = "YOUR OWN PHONE NUMBER VERIFIED WITH TWILIO"

# Stock and company configuration
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API endpoints and keys
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

# Fetch stock data from Alpha Vantage
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]  # Convert to list for easy access

# Get closing prices for yesterday and day before
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Calculate price difference and trend indicator
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = "🔺" if difference > 0 else "🔻"

# Calculate percentage change
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

# If price change exceeds 1%, fetch and send news alerts
if abs(diff_percent) > 1:
    # Fetch news articles about the company
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Get first 3 articles
    three_articles = articles[:3]
    print(three_articles)

    # Format articles for SMS messages
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]
    print(formatted_articles)

    # Send SMS alerts via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
