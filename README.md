# 🎵 Streaming Playlist & Genre Analysis

This project analyzes streaming playlists, artist genres, and song patterns to uncover relationships and trends between artists, genres, and listening habits. It includes tools to sort genres, visualize playlist connections, and recommend playlists or songs based on streaming patterns.

## 📁 Contents
- `artist_genres.json` — Mapping of artists to their genres.
- `playlist_connections.json` — Graph of playlists and their connections.
- `generated_playlists.json` — Sample playlists with song titles.
- `recommended_playlist.json` — Example recommended playlist.
- `sorted_streaming_song_patterns.json` — Pre-processed song pattern data.
- `streaming_song_patterns.json` — Raw streaming song pattern data.
- `genre_sorting.py` — Script to sort and process artist genres.
- `streaming_analysis.py` — Script to analyze playlist graphs and recommend playlists.
- `requirements.txt` — Python dependencies.

## 🚀 Features
✅ Sort artists by genre.  
✅ Visualize connections between playlists as a graph.  
✅ Recommend playlists or songs based on user streaming patterns.  
✅ Analyze co-occurrence of songs across playlists.

## 🔧 Setup
1️⃣ Clone this repository:

    git clone https://github.com/antoniodeoliveirasegura//Spotify-Listening-Pattern-Analyzer/.git
    cd Spotify-Listening-Pattern-Analyzer

2️⃣ Install dependencies:

    pip install -r requirements.txt

3️⃣ (Optional) Create a `.env` file if you want to use Spotipy or other APIs and add your credentials there.

## 📊 Usage
Run the scripts:

    python genre_sorting.py
    python streaming_analysis.py

These will process the JSON data and output sorted genres, graphs, or recommendations.

## 📝 Notes
- API keys or tokens are **not included**. Make sure to set up your own if required.
- The dataset contains only public song and artist names — no personal or sensitive data.

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

# 📄 LICENSE

MIT License  

Copyright (c) 2025 Antonio De Oliveira Segura

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
