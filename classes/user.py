"""
module to create a layer of abstraction between main program and the spotipy api

input: a spotipy user object

output: User object
"""
import spotipy
from .playlist import Playlist
from spotipy.oauth2 import SpotifyOAuth


class User:
    
    def __init__(self, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, SCOPE):
        self.user = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                              client_secret=SPOTIPY_CLIENT_SECRET,
                                                              redirect_uri=SPOTIPY_REDIRECT_URI,
                                                              scope=SCOPE))
        self.display_name = self.user.me()['display_name']

        self.id = self.user.me()['id']

    def __str__(self):
        display_name = self.display_name
        return display_name

    #def get_user_id(self):
        #user_id = self.id
        #return user_id

    #def user_owned_playlist(self, playlist):
        #return self.sp.get

    #def get_track_ids_from_playlist(self, playlist_id):
        #playlist_tracks = self.sp.playlist_tracks(playlist_id)
        #track_ids = []
        #while playlist_tracks:
            #for playlist_track in playlist_tracks['items']:
                #track_ids.append(playlist_track['track']['id'])
            #if playlist_tracks['next']:
                #playlist_tracks = self.sp.next(playlist_tracks)
            #else:
                #playlist_tracks = None
        #return track_ids

     #gets track ids for all songs that are on user owned playlists
    #def get_all_user_owned_tracks(self):
        #playlists = self.sp.current_user_playlists()
        #all_track_ids = []
        #while playlists:
            #for playlist in playlists['items']:
                #playlist = Playlist(playlist)
                #playlist_owner_id = playlist.get_playlist_owner_id()
                #if playlist_owner_id == self.get_user_id():
                    #playlist_id = playlist.get_playlist_id()
                    #all_track_ids.extend(self.get_track_ids_from_playlist(playlist_id))
            #if playlists['next']:
                #playlists = self.sp.next(playlists)
            #else:
                #playlists = None
        #return all_track_ids

                


