import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

def main():

	scope = 'playlist-modify-public'
	username = 'haydnvn'

	token = SpotifyOAuth(scope = scope,username = username)

	spotifyObject = spotipy.Spotify(auth_manager = token)

	#create

	playlist_name = "Weather"
	playlist_description = "day"

	#spotifyObject.user_playlist_create(user = username,name = playlist_name, public = True ,description = playlist_description)
	



	#user_input = (input('name of song:'))
	#while user_input != 'quit':
	#	result = spotifyObject.search(q=user_input,limit=1)
	#	print(json.dumps(result,sort_keys=4,indent=4))
	#	track1 = result['tracks']['items'][0]['uri']
	#	#print(spotifyObject.audio_features(track1))
	#	#print(result["tracks"])
	#	user_input = input('name of song:')
	
	
	run("Rain",["rock"])
	
def makePlaylist(e_c,d_c,t_c,m_c,genseed):
	scope = 'playlist-modify-public'
	username = 'haydnvn'
	token = SpotifyOAuth(scope = scope,username = username)
	spotifyObject = spotipy.Spotify(auth_manager = token)

	lim = 20
	#change rec genre list
	recc = spotifyObject.recommendations(seed_genres=genseed,limit=lim)
	
	songs = []
	#the one that works index on the 0 and get uri to add to playlist
	for x in range(lim):
		uri = recc["tracks"][x]["uri"]
		#print(recc["tracks"][x]["name"]) #change name for uri
		features = spotifyObject.audio_features(uri)
		energy = features[0]["energy"]
		dance = features[0]["danceability"]
		tempo = features[0]["tempo"]
		mood = features[0]["valence"]
		songs.append(uri)
		if(energy > e_c[0] and energy < e_c[1] and dance > d_c[0] and dance < d_c[1] and tempo > t_c[0] and tempo < t_c[1] and mood > m_c[0] and mood < m_c[1]):
			print(str(energy) + " " +str(dance) + " " + str(tempo))	
			print(recc["tracks"][x]["name"])
		else:
			print("bad")
			print("en: " + str(energy) + " dance: " +str(dance) + " tempo: " + str(tempo) + "mood: " + str(mood))
	
	print(songs)
	spotifyObject.playlist_add_items(playlist_id="4oHK732Nnt1yl90UdxQOBW",items=songs)


#adjusts based on the cut offs and genres of the user
def run(mainType,user_genres):
	#energy [min,max]
	#dance [min,max]
	#tempo [min,max]
	#mood [min,max] (valence)
	#genre seed
	
	if(mainType == "Rain" or mainType == "Drizzle" or mainType == "Thunderstorm"):
		energy_cutoffs = [0.5,1]
		dance_cutoffs  = [0,0.7]
		tempo_cutoffs = [0,100]
		mood_cutoffs = [0,0.6]
		gen = user_genres
		gen.append("rainy-day")
		
	elif(mainType == "Snow"):
		energy_cutoffs = [0,0.5]
		dance_cutoffs  = [0,0.5]
		tempo_cutoffs = [0,76]
		mood_cutoffs = [0,0.5]
		gen = user_genres
	elif(mainType == "Clear"):
		energy_cutoffs = [0.5,1]
		dance_cutoffs  = [.3,1]
		tempo_cutoffs = [76,200]
		mood_cutoffs = [0.5,1]
		gen = user_genres
	elif(mainType == "Clouds"):
		energy_cutoffs = [0.25,0.75]
		dance_cutoffs  = [0.25,0.75]
		tempo_cutoffs = [40,115]
		mood_cutoffs = [0.25,0.65]
		gen = user_genres

	makePlaylist(e_c=energy_cutoffs,d_c=dance_cutoffs,t_c=tempo_cutoffs,m_c=mood_cutoffs,genseed=gen)

if __name__=="__main__":
	main()
