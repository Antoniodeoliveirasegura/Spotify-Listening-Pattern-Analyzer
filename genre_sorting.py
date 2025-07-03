import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

# Load your client credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
))

# Load unique artist names from your data
with open("sorted_streaming_song_patterns.json", "r") as f:
    data = json.load(f)

unique_artists = set()
for song in data:
    try:
        title, artist = song.split(" - ")
        unique_artists.add(artist.strip())
    except:
        pass

artist_genres = {}
for artist in unique_artists:
    try:
        results = sp.search(q=f"artist:{artist}", type='artist', limit=1)
        items = results['artists']['items']
        if items:
            genres = items[0]['genres']
            artist_genres[artist] = genres
        else:
            artist_genres[artist] = ["Unknown"]
    except Exception as e:
        artist_genres[artist] = ["Unknown"]
        print(f"Failed to get genre for {artist}: {e}")
    time.sleep(0.2)  # Respect API rate limits

# Save the genre mapping
with open("artist_genres.json", "w") as f:
    json.dump(artist_genres, f, indent=4)

print("✅ Genre mapping complete!")
