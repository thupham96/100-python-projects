# Day 49: 💼 Python Job Scraper → SimplyHired Listings Bot 🕵️‍♂️🧑‍💻

Automate your job hunt with this Python script! Using Selenium, this bot scrapes real-time job listings for "Python Developer" roles from SimplyHired and prints the job title along with the direct link.

## How It Works

1. **URL Targeting**: Opens the SimplyHired job search page for Python Developer roles.
2. **Page Parsing**: Waits for the page to load and grabs all job listing containers.
3. **Data Extraction**: Extracts job titles and links from each container.
4. **Error Handling**: Skips over broken or malformed job cards gracefully.
5. **Output Display**: Prints each job title and clickable link in the console.

## Features

* 🔍 Scrapes job titles and links from SimplyHired
* ⚙️ Uses Selenium to automate browser and content extraction
* 🚫 Skips broken listings with error handling
* 🧭 Easily customizable for different job titles or locations

## How to Use

1. Clone the repo and install Selenium:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day49_JobScraper
   pip install selenium
   ```

2. Download and set up [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatible with your Chrome version, and add it to your PATH.

3. Run the bot:

   ```bash
   python main.py
   ```

## Technologies Used

* Python 3
* `selenium` for browser automation
* Chrome + ChromeDriver

## Example Output

```
Python Developer → https://www.simplyhired.com/job/abcd1234
Backend Engineer (Python) → https://www.simplyhired.com/job/xyz9876
...
```

## What I Learned

* Automating job searches using Selenium
* Navigating complex web elements with CSS selectors
* Gracefully handling scraping errors
* Building a foundation for more advanced job tracking bots

---

💡 A perfect starting point for anyone looking to automate tedious job searches and break into tech — let Python help you get hired!
