# Day 45: 🎬 Top 100 Movies Web Scraper with Years 📽️🗓️

Extract and save the **Top 100 Movies** from a curated list using Python and BeautifulSoup! This script scrapes movie titles and their release years from a web archive of Empire Online’s top 100 films.

## How It Works

1. **Web Request**: Sends a GET request to a snapshot of the Empire Online Top 100 Movies page.
2. **HTML Parsing**: Uses BeautifulSoup to parse the webpage and extract movie titles and release years.
3. **Data Extraction**: Matches titles from `<h3>` elements and years from `<p><strong>` tags.
4. **Save to File**: Writes the results in reverse order to a `.txt` file for easy reading.

## Features

* 🌐 Web scraping using `requests` and `BeautifulSoup`
* 🧠 Handles missing data with try/except
* 📄 Saves clean movie list with release years
* 📚 Great beginner project for learning web scraping

## Example Output (movies\_with\_years.txt)

```
1) The Godfather (1972)
2) The Empire Strikes Back (Unknown)
...
100) Stand By Me (1986)
```

## How to Use

1. Clone or download the project:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day45_MovieWebScraper
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. Check the output:

   * Open `movies_with_years.txt` to see the scraped list in order.

## Technologies Used

* Python 3
* `requests` for making HTTP requests
* `BeautifulSoup` (bs4) for parsing HTML

## What I Learned

* How to perform web scraping with BeautifulSoup
* CSS selectors to extract specific HTML elements
* Handling missing or inconsistent data safely
* Writing and formatting output to a text file

---

Explore classic cinema and level up your Python scraping skills with this **Top Movies Web Scraper**! 🎥🍿
