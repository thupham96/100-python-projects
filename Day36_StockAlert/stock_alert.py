import requests
from twilio.rest import Client
import datetime

# Skip weekends
if datetime.datetime.today().weekday() >= 5:
    print("Weekend — market is closed. No alerts sent.")
    exit()

# Twilio credentials (replace with environment variables in production)
account_sid = "your_account_sid"
auth_token = "your_auth_token"

# Stock and news API details
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "your_stock_api_key"
NEWS_API_KEY = "your_news_api_key"

# API endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Step 1: Fetch daily stock data from Alpha Vantage
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]
dates = sorted(data.keys(), reverse=True)

# Step 2: Extract the closing prices for yesterday and the day before
yesterday_close = float(data[dates[0]]["4. close"])
day_before_close = float(data[dates[1]]["4. close"])

# Step 3: Calculate the absolute percentage change
difference = yesterday_close - day_before_close
change_percent = abs(difference / day_before_close) * 100
up_down_symbol = "🔺" if difference > 0 else "🔻"

# Step 4: If the change is significant, fetch related news
if change_percent >= 4:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "sortBy": "publishedAt"
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json().get("articles", [])[:3]  # Top 3 articles

    # Step 5: Format news messages
    article_messages = [
        f"{STOCK_NAME}: {up_down_symbol}{change_percent:.2f}%\n"
        f"Headline: {article.get('title')}\n"
        f"Brief: {article.get('description')}"
        for article in articles
    ]

    # Step 6: Send each message via WhatsApp using Twilio
    client = Client(account_sid, auth_token)
    for i, message_text in enumerate(article_messages, start=1):
        print(f"\nNews {i}:\n{message_text}")
        message = client.messages.create(
            from_='whatsapp:your_twilio_number',   # Twilio sandbox number
            body=f"\nNews {i}:\n{message_text}",
            to='whatsapp:recipient_verified_number'
        )
        print("Message status:", message.status)

else:
    print(f"Change was {change_percent:.2f}%, no news fetch needed.")
