# Day 93: Audible Audiobook Scraper – Python Web Scraping with BeautifulSoup

This project scrapes audiobook listings from [Audible.com](https://www.audible.com/) and extracts essential metadata such as title, author, narrator, runtime, release date, language, and more. It saves the data into a clean `.csv` file — perfect for cataloging, filtering, or personal research.

---

## Features

* Scrapes **audiobook listings** from Audible search results
* Extracts:

  * **Title**
  * **Author**
  * **Subtitle**
  * **Narrator**
  * **Runtime**
  * **Language**
  * **Release Date**
  * **Link**
* Handles missing fields gracefully with `"N/A"` fallback
* Outputs results to a structured **CSV file**
* Includes **console logging** for real-time feedback
* Encodes output using **UTF-8** for compatibility

---

## Technologies Used

* **Python**
* **requests** – for sending HTTP requests
* **BeautifulSoup (bs4)** – for HTML parsing and data extraction
* **csv** – for writing structured data to a CSV file

---

## How to Run

1. **Clone the repository or copy the code**:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day93_Audible_Scraper
   ```

2. **Install dependencies** (use a virtual environment if preferred):

   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the script**:

   ```bash
   python main.py
   ```

4. **View your results**:

   * The script will create an `audible_books.csv` file with all extracted data.
   * You’ll also see the data printed in the console as it's scraped.

---

## Example Output (Console)

```
Title: Burn Book - Author: Kara Swisher - Subtitle: A Tech Love Story
Narrator: Kara Swisher - 7 hrs and 40 mins - Language: English
Release date: 02-27-24
Link: https://www.audible.com/search?keywords=book&node=18573211011
```

---

## Output File Format (`audible_books.csv`)

| Title     | Author       | Subtitle          | Narrator     | Runtime        | Language | Release Date | Link |
| --------- | ------------ | ----------------- | ------------ | -------------- | -------- | ------------ | ---- |
| Burn Book | Kara Swisher | A Tech Love Story | Kara Swisher | 7 hrs 40 mins  | English  | 02-27-24     | ...  |

---

## What I Learned

* How to **scrape dynamic web content** using BeautifulSoup
* Handling **missing or partial HTML elements** gracefully
* Using **CSV writer** to create structured data exports
* Parsing Audible's HTML layout and navigating nested tags
* Efficient **data collection and output formatting** in Python
