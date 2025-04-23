# Day 36: Stock Alert with Twilio 📈📲

Stay on top of the market with **Stock Alert** – a Python script that checks daily stock changes and sends breaking news via WhatsApp using the Twilio API. Perfect for traders or curious investors who want instant insights! 📰💰

## How It Works

1. **Daily Stock Monitoring**: Pulls closing prices for the last two trading days from Alpha Vantage.
2. **Change Detection**: Calculates the percentage change and checks if it’s significant (≥ 4%).
3. **News Fetching**: If the change is notable, fetches top 3 news articles about the company using NewsAPI.
4. **WhatsApp Notification**: Sends formatted summaries of each news item to your WhatsApp via Twilio.

## Example Output

- **Stock**: TSLA  
- **Change**: 🔺5.02%  
- **Headline**: Tesla announces new AI initiative  
- **Brief**: Tesla unveils a bold new step into autonomous tech with its AI-powered strategy...

- **Delivery**: Sent directly to your WhatsApp using the Twilio number.

## Features

- 📉 Tracks real-time stock data from Alpha Vantage  
- 📊 Auto-calculates % change in stock price  
- 📰 Fetches news summaries from NewsAPI  
- 📲 Sends WhatsApp alerts via Twilio  
- ⛔ Skips weekends (market closed)

## How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/thupham96/python-projects.git
   cd Day36_StockAlert
   ```

2. Replace credentials with your own (use environment variables for safety):
   - `account_sid`, `auth_token` from Twilio
   - `STOCK_API_KEY` from Alpha Vantage
   - `NEWS_API_KEY` from NewsAPI

3. Run the script:
   ```bash
   python stock_alert.py
   ```

## Technologies Used

- Python 3
- `requests` for API communication
- `twilio` for WhatsApp messaging
- Alpha Vantage API (https://www.alphavantage.co/)
- NewsAPI (https://newsapi.org/)
- Twilio WhatsApp Sandbox

## What I Learned

- Analyzing financial time-series data
- Integrating multiple APIs into one workflow
- Automating conditional notifications
- Sending real-time alerts via WhatsApp
- Skipping logic based on weekdays for stock markets

Be the first to know when your favorite stock makes a move — with **Stock Alert**, your investment insights come straight to your chat. 🚀📬
