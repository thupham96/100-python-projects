from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set Chrome options to keep the browser open after the script ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Launch Chrome browser with specified options
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find the main cookie element to click
cookie = driver.find_element(By.ID, value="cookie")

# Function to buy the most expensive item that can be afforded
def buy_item():
    # Get the current amount of cookies (as an integer)
    money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))

    # Get all store items
    store = driver.find_elements(By.CSS_SELECTOR, value="#store div")

    chosen_item = None
    for item in store:
        try:
            # Get the item's name and price
            item_name = item.find_element(By.CSS_SELECTOR, "b").text
            if "-" in item_name:
                item_price = int(item_name.split("-")[1].strip().replace(",", ""))
                # Choose the most expensive item affordable
                if item_price <= money:
                    chosen_item = item
        except Exception:
            continue

    # Click to buy the chosen item
    if chosen_item:
        chosen_item.click()

# Timing configuration
time_out = 10  # initial timeout duration
time_start = time.time()

# Main loop to click cookie and buy upgrades
while True:
    if time.time() < time_start + time_out:
        for _ in range(10): cookie.click()
    else:
        buy_item()
        time_out += 10  # increase the timeout for the next check

    # After 5 minutes, stop and print cookies per second
    if time_out == 300:
        cookies_per_second = driver.find_element(By.ID, value="cps").text
        cookies_per_second = cookies_per_second.split(":")[1].strip()
        print(f"Cookies per second: {cookies_per_second}")
        break
