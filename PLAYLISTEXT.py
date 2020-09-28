import sys
import os
import string
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
os.system('cls' if os.name == 'nt' else 'clear')

#Parameters
cid = os.environ.get('SPOTIFY_ID')
secret = os.environ.get('SPOTIFY_SECRET')
username =  os.environ.get('SPOTIFY_USER')
scope = 'user-library-read, playlist-modify-public'
redirect_uri = 'http://127.0.0.1:80'
playlist_name = 'PLAYLISTEXT'

def Autentication():
    try:
        token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret, redirect_uri=redirect_uri)
    except:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret, redirect_uri=redirect_uri)
    if token:
        sp = spotipy.Spotify(auth=token)
    else:
        sys.exit()
    return sp

def GetTracksIDs():
    track_ids = []
    User_input = input('Insert phrase: ')
    if not User_input: #error if imput empty
        print('ERROR - Empty input')
        sys.exit()
    print('\nMusics found:')    
    songs = User_input.translate(str.maketrans('', '', string.punctuation)).split(' ') #remove ponctuations from input
    
    for i in range(len(songs)):
        songs[i] = songs[i].capitalize() #Most musics on Spotify starts with capital letters, so capitalize them all!
        results = sp.search(q=songs[i], limit=50, type='track') #get 50 responses (max) since first one isn't always accurate      

        if results['tracks']['total'] == 0: #if tracks aren't exactly on spotify as queried
                print('ERROR with the word %s' %songs[i])
                sys.exit()
        else:
            for j in range(len(results['tracks']['items'])):
                if results['tracks']['items'][j]['name'] ==  songs[i]: #get right response
                    track_ids.append(results['tracks']['items'][j]['id']) #append track id
                    print(results['tracks']['items'][j]['name'])
                    break #don't want repeats of a sample ex: different versions
                else:
                    continue
    if not track_ids: #error if imput empty
        print('ERROR - No music found')
        sys.exit()

    return track_ids,User_input

def CreatePlaylist(): 
    sp.user_playlist_create(username, name = playlist_name, public=True, description = playlist_description)

def GetPlaylistID():
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            playlist_id = playlist['id']
    return playlist_id

def addMusicToPlaylist():
    sp.user_playlist_add_tracks(username, playlist_id, track_ids)

if __name__ == '__main__':
    sp = Autentication()
    track_info = GetTracksIDs()
    track_ids = track_info[0]
    playlist_description = track_info[1]
    x = input('\nCreate Playlist? (y/n) \n')
    if x != 'y':
        sys.exit()
    CreatePlaylist()
    playlist_id = GetPlaylistID()
    addMusicToPlaylist()
    print('\nPlaylist created with success!\n')