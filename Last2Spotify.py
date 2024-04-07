import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Last.fm API credentials
LASTFM_API_KEY = 'YOUR_LASTFM_API_KEY'
LASTFM_USERNAME = 'YOUR_LASTFM_USERNAME'
LIMIT = 100  # Change this value to adjust the limit of tracks

# Spotify API credentials
SPOTIPY_CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'https://example.com'

# Authenticate with Last.fm
response = requests.get(f'http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={LASTFM_USERNAME}&api_key={LASTFM_API_KEY}&format=json&limit={LIMIT}')
data = response.json()

# Extract track names from Last.fm response
track_names = [track['name'] for track in data['toptracks']['track']]

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='playlist-modify-private'))

# Search for tracks on Spotify
track_uris = []
for track_name in track_names:
    result = sp.search(q=track_name, limit=1)
    if result['tracks']['items']:
        track_uris.append(result['tracks']['items'][0]['uri'])

# Create a playlist on Spotify
playlist = sp.user_playlist_create(user=sp.me()['id'], name='My Top Tracks', public=False)

# Add tracks to the playlist
sp.user_playlist_add_tracks(user=sp.me()['id'], playlist_id=playlist['id'], tracks=track_uris)
