from bs4 import BeautifulSoup
import requests

movies_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(movies_url)
soup = BeautifulSoup(response.text, "html.parser")

# Select each article block containing title and description
movie_blocks = soup.select(".article-title-description__text")
movie_data = []

for block in movie_blocks:
    title_tag = block.select_one("h3.title")
    year_tag = block.select_one(".descriptionWrapper p strong")

    title = title_tag.get_text(strip=True) if title_tag else "Untitled"
    year = year_tag.get_text(strip=True) if year_tag else "Unknown"

    movie_data.append(f"{title} ({year})")

# Write to file in reverse order
with open("movies_with_years.txt", "w", encoding="utf-8") as file:
    for movie in reversed(movie_data):
        file.write(movie + "\n")
