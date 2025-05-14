import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials (set these in your environment variables)
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Get user input for the date
date_requested = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Set up headers for Billboard request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

# Fetch Billboard Hot 100 for the given date
billboard_url = f"https://www.billboard.com/charts/hot-100/{date_requested}/"
response = requests.get(billboard_url, headers=headers)
response.raise_for_status()

# Parse HTML to extract song titles
soup = BeautifulSoup(response.text, "html.parser")
song_tags = soup.select(".o-chart-results-list-row-container h3.c-title.a-font-primary-bold-s")
song_titles = [tag.get_text(strip=True) for tag in song_tags]

print(f"🎵 Found {len(song_titles)} songs from {date_requested}")

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private playlist-modify-public",
    cache_path="token.txt",
    show_dialog=True
))

# Get user ID and check if playlist exists
user_id = sp.current_user()["id"]
print(f"✅ Authenticated as: {user_id}")

playlist_id = ""
existing_playlists = sp.current_user_playlists()["items"]
for playlist in existing_playlists:
    if playlist["name"] == date_requested:
        playlist_id = playlist["id"]
        print(f"📂 Playlist already exists: {playlist_id}")
        break

if playlist_id == "":
    playlist = sp.user_playlist_create(user=user_id, name=date_requested)
    playlist_id = playlist["id"]
    print(f"✅ Playlist created: {playlist_id}")

# Fetch existing track URIs in the playlist
existing_uris = []
offset = 0
while True:
    response = sp.playlist_items(playlist_id, offset=offset, fields="items.track.uri,total", additional_types=['track'])
    items = response["items"]
    if not items:
        break
    existing_uris.extend([item["track"]["uri"] for item in items if item["track"]])
    offset += len(items)

# Search and collect new Spotify URIs (skip if already in playlist)
new_song_uris = []
for title in song_titles:
    result = sp.search(q=f"track:{title}", type="track", limit=1)
    try:
        uri = result['tracks']['items'][0]['uri']
        if uri not in existing_uris:
            new_song_uris.append(uri)
            print(f"✅ Adding: {title}")
        else:
            print(f"⏭️ Skipped (already in playlist): {title}")
    except IndexError:
        print(f"❌ Not found: {title}")

# Add only new songs to the playlist
if new_song_uris:
    sp.playlist_add_items(playlist_id=playlist_id, items=new_song_uris)
    print(f"✅ Added {len(new_song_uris)} new songs to playlist.")
else:
    print("⚠️ No new songs to add.")
