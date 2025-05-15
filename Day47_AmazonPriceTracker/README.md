# Day 47: 🛒 Amazon Price Tracker → Email Alert System 💸📬

Stay on top of online deals with this Python script! It automatically monitors the price of a specific Amazon product and sends you an email alert when the price drops below your target.

## How It Works

1. **Target Price**: Define your price threshold and product details.
2. **Web Scraping**: Sends a request to Amazon and parses the product page using `BeautifulSoup`.
3. **Price Detection**: Extracts the current price from the page.
4. **Email Notification**: Sends an email if the price is below the set target.
5. **Environment Variables**: Keeps your credentials safe using `dotenv`.

## Features

* 🔍 Scrapes real-time price from Amazon product page
* 📬 Sends an email when your desired deal is live
* 🔐 Uses environment variables for secure credentials
* ⚠️ Skips alert if price is still too high
* 🖥️ Simple to configure and run manually or via scheduler (e.g., cron)

## How to Use

1. Clone the repo and install dependencies:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day47_AmazonPriceTracker
   pip install requests beautifulsoup4 python-dotenv
   ```

2. Create a `.env` file with:

   ```
   MY_EMAIL=youremail@gmail.com
   MY_EMAIL_PASSWORD=yourpassword
   ```

3. Run the script:

   ```bash
   python main.py
   ```

## Technologies Used

* Python 3
* `requests` + `BeautifulSoup` for web scraping
* `smtplib` for email delivery
* `dotenv` for managing environment variables

## Example Output

```
Price found: $97.99
✅ Deal found below target!
📬 Email sent successfully.
```

## What I Learned

* Web scraping product data using request headers and CSS selectors
* Working with SMTP and email formatting in Python
* Handling environment variables securely with `dotenv`
* Building a practical automation tool for real-world use

---

💡 Never miss a deal again — let your script check the price for you!
