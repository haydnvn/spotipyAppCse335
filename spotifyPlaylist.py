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

lim = 20
#change rec genre list
recc = spotifyObject.recommendations(seed_genres=["rainy-day","rock"],limit=lim)
#print(json.dumps(recc,sort_keys=4,indent=4))

g = spotifyObject.recommendation_genre_seeds()
print(json.dumps(g,sort_keys=4,indent=4))
#the one that works index on the 0 and get uri to add to playlist
for x in range(lim):
	print(recc["tracks"][x]["name"])



user_input = (input('name of song:'))
while user_input != 'quit':
	result = spotifyObject.search(q=user_input,limit=1)
	print("\n\n\n")
	print(json.dumps(result,sort_keys=4,indent=4))
	track1 = result['tracks']['items'][0]['uri']
	#print(spotifyObject.audio_features(track1))
	#print(result["tracks"])
	user_input = input('name of song:')
