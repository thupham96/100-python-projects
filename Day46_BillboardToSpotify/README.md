# Day 46: 🎶 Billboard Time Machine → Spotify Playlist Generator 📅➡️🎧

Travel back in time and relive the music of your chosen day! This Python script scrapes the **Billboard Hot 100** from a specific date and automatically creates (or updates) a **Spotify playlist** with matching songs using the Spotify Web API.

## How It Works

1. **Date Input**: Prompts the user to enter a date (YYYY-MM-DD).
2. **Web Scraping**: Extracts top 100 song titles from Billboard’s Hot 100 chart using `requests` + `BeautifulSoup`.
3. **Spotify Auth**: Authenticates via Spotipy to access user playlists.
4. **Playlist Creation**: Checks if a playlist for that date exists, creates one if not.
5. **Track Matching**: Searches Spotify for each song, avoiding duplicates.
6. **Song Upload**: Adds all found songs to the playlist!

## Features

* 🕰️ Travel to any musical era (since 1958)
* 🧠 Smart duplicate checking
* 🤖 Spotify playlist automation
* 🧼 Clean handling of missing or unmatched tracks
* 🎯 Minimal setup with real-time feedback

## How to Use

1. Clone the repo and install dependencies:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day46_BillboardToSpotify
   pip install requests beautifulsoup4 spotipy
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. Authorize Spotify access in your browser and watch your playlist get built!

## Technologies Used

* Python 3
* `requests` + `BeautifulSoup` for web scraping
* `spotipy` for Spotify API integration
* Billboard Hot 100 (via HTML scraping)

## Example Output

```
🎵 Found 100 songs from 1999-07-10
✅ Authenticated as: your_username
✅ Playlist created: 5n2XYZ...
✅ Adding: Genie In a Bottle
⏭️ Skipped (already in playlist): Livin' La Vida Loca
❌ Not found: Some Rare Song
✅ Added 87 new songs to playlist.
```

## What I Learned

* HTML scraping with CSS selectors
* OAuth2 and Spotify API integration
* Searching & filtering with Spotipy
* Building interactive command-line tools

---

🎉 Turn music nostalgia into a custom Spotify playlist with just one script!
