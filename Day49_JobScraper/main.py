from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set the search URL
JOBS_SEARCH_URL = "https://www.simplyhired.com/search?q=python+developer"

# Set Chrome options to keep browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Launch browser
driver = webdriver.Chrome(options=chrome_options)
driver.get(JOBS_SEARCH_URL)

time.sleep(3)  # allow time for page to load

# Get all job containers
job_listings = driver.find_elements(By.CSS_SELECTOR, "#job-list > li")

for job in job_listings:
    try:
        title_element = job.find_element(By.CSS_SELECTOR, "h2 a")
        title = title_element.text
        link = title_element.get_attribute("href")
        print(f"{title} → {link}")
    except Exception as e:
        print("Skipped a job due to error:", e)

driver.quit()
