import requests
from bs4 import BeautifulSoup
import csv

# Target URL
url = "https://www.audible.com/search?keywords=book&node=18573211011"

# Send GET request
response = requests.get(url)
response.raise_for_status()

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract book titles
books = soup.find_all("li", class_="bc-list-item productListItem")
with open("audible_books.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Author", "Subtitle", "Narrator", "Runtime", "Language", "Release Date", "Link"])
    for book in books:
        title_tag = book.find("h3", class_="bc-heading")
        book_title = title_tag.find("a").get_text(strip=True) if title_tag else "N/A"
        book_link = title_tag.find("a")['href'] if title_tag else "N/A"

        author_tag = book.find("li", class_="bc-list-item authorLabel")
        author = author_tag.find("a").get_text(strip=True) if author_tag else "N/A"

        subtitle_tag = book.find("li", class_="bc-list-item subtitle")
        subtitle = subtitle_tag.find("span").get_text(strip=True) if subtitle_tag else "N/A"

        narrator_tag = book.find("li", class_="bc-list-item narratorLabel")
        narrator = narrator_tag.find("a").get_text(strip=True) if narrator_tag else "N/A"

        runtime_tag = book.find("li", class_="bc-list-item runtimeLabel")
        runtime = runtime_tag.find("span").get_text(strip=True) if runtime_tag else "N/A"

        release_date_tag = book.find("li", class_="bc-list-item releaseDateLabel")
        release_date = release_date_tag.find("span").get_text(strip=True) if release_date_tag else "N/A"
        release_date = release_date.replace("Release date:", "").strip()

        language_tag = book.find("li", class_="bc-list-item languageLabel")
        language = language_tag.find("span").get_text(strip=True) if language_tag else "N/A"
        language = language.replace("Language:", "").strip()

        writer.writerow([book_title, author, subtitle, narrator, runtime, language, release_date, url])

        print(f"Title: {book_title} - Author: {author} - Subtitle: {subtitle}")
        print(f"Narrator: {narrator} - {runtime} - Language: {language}")
        print(f"Release date: {release_date}")
        print(f"Link: {url}")
        print("\n")
