import pandas as pd

def load_data():
    return pd.read_csv('data/songs.csv')

def recommend_songs(genre=None, artist=None, num_recommendations=5):
    songs = load_data()
    
    if genre:
        songs = songs[songs['playlist_genre'].str.contains(genre, case=False, na=False)]

    if artist:
        songs = songs[songs['track_artist'].str.contains(artist, case=False, na=False)]

    # Remove duplicates based on 'track_id' (or 'track_name' and 'track_artist')
    songs = songs.drop_duplicates(subset=['track_id'])  # or use ['track_name', 'track_artist']

    # Sort by popularity and return the top recommendations
    return songs.sort_values(by='track_popularity', ascending=False).head(num_recommendations)
