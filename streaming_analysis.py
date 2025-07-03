import os
import json
import random
from collections import defaultdict

# Load song transition data
with open("sorted_streaming_song_patterns.json", "r", encoding="utf-8") as f:
    song_patterns = json.load(f)

# Configuration
NUM_PLAYLISTS = 100
PLAYLIST_LENGTH = 50  # Max length of each playlist
OUTPUT_DIR = "playlists"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to generate a playlist
def generate_playlist(start_song, song_patterns, max_length=50):
    playlist = [start_song]
    seen_songs = set(playlist)

    while len(playlist) < max_length:
        current_song = playlist[-1]
        
        # Get next possible songs sorted by frequency
        next_songs = list(song_patterns.get(current_song, {}).items())
        
        if not next_songs:
            break  # Stop if no next songs are available
        
        # Apply weighted randomness to diversify paths
        next_songs = sorted(next_songs, key=lambda x: x[1], reverse=True)
        weighted_choices = [song for song, weight in next_songs for _ in range(weight)]
        next_song = random.choice(weighted_choices) if weighted_choices else None
        
        if next_song and next_song not in seen_songs:
            playlist.append(next_song)
            seen_songs.add(next_song)
        else:
            break  # Stop if no more unique songs are available

    return playlist

# Generate multiple playlists
generated_playlists = {}
playlist_connections = defaultdict(list)
all_songs = list(song_patterns.keys())

for i in range(NUM_PLAYLISTS):
    start_song = random.choice(all_songs)  # Choose a random starting song
    playlist = generate_playlist(start_song, song_patterns, max_length=PLAYLIST_LENGTH)
    
    # Save the playlist
    playlist_filename = os.path.join(OUTPUT_DIR, f"playlist_{i+1}.json")
    with open(playlist_filename, "w", encoding="utf-8") as f:
        json.dump(playlist, f, indent=4)
    
    # Store the playlist in memory
    generated_playlists[f"Playlist_{i+1}"] = playlist

    # Connect playlists if they share songs
    for j in range(i):  # Compare with previous playlists
        shared_songs = set(generated_playlists[f"Playlist_{j+1}"]) & set(playlist)
        if shared_songs:
            playlist_connections[f"Playlist_{i+1}"].append(f"Playlist_{j+1}")
            playlist_connections[f"Playlist_{j+1}"].append(f"Playlist_{i+1}")

# Save all playlists in one JSON file
with open("generated_playlists.json", "w", encoding="utf-8") as f:
    json.dump(generated_playlists, f, indent=4)

# Save playlist connections as JSON
with open("playlist_connections.json", "w", encoding="utf-8") as f:
    json.dump(playlist_connections, f, indent=4)

print(f"✅ {NUM_PLAYLISTS} playlists generated in the '{OUTPUT_DIR}' folder!")
print("✅ Playlist connections saved to 'playlist_connections.json'!")
