import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = 'haydnvn'

token = SpotifyOAuth(scope = scope,username = username)

spotifyObject = spotipy.Spotify(auth_manager = token)

#create

playlist_name = "Weather"
playlist_description = "day"

spotifyObject.user_playlist_create(user = username,name = playlist_name, public = True ,description = playlist_description)
