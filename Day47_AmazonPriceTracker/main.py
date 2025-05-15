import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

TARGET_PRICE = 100
MY_EMAIL = os.getenv("MY_EMAIL")
MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("MY_EMAIL")

PRODUCT_NAME = "Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker..."

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,vi;q=0.7"
}
amazon_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response = requests.get(url=amazon_url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
price_tag = soup.select_one(".aok-offscreen")

if price_tag:
    try:
        price_text = price_tag.get_text().strip()
        price = float(price_text.replace("$", ""))
        print(f"Price found: ${price}")

        if price < TARGET_PRICE:
            email_body = f"{PRODUCT_NAME} is now ${price}\n{amazon_url}"
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=RECIPIENT_EMAIL,
                    msg=f"Subject:Amazon Price Alert!\n\n{email_body}"
                )
                print("Email sent successfully.")
        else:
            print(f"Price ${price} is still above target.")
    except Exception as e:
        print("Error processing price or sending email:", e)
else:
    print("Price tag not found.")
