"""
module to create a layer of abstraction between main program and the spotipy api

input: a spotipy user object

output: User object
"""
import spotipy
from .playlist import Playlist
from spotipy.oauth2 import SpotifyOAuth


class User:

    def __init__(self, SCOPE):
        self.user = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))
        self.user_object = self.user.me()
        self.id = self.user_object['id']
        self.display_name = self.user_object['display_name']
        self.external_urls = self.user_object['external_urls']
        self.followers_object = self.user_object['followers']
        self.href = self.user_object['href']
        self.uri = self.user_object['uri']

    def __str__(self):
        return f"{self.display_name}"
        

    def get_id(self):
        return self.id

    def get_display_name(self):
        return self.display_name

    def get_external_urls(self):
        return self.external_urls

    def get_follower_count(self):
        return self.followers_object['total']

    def get_href(self):
        return self.href

    def get_uri(self):
        return self.uri

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

                


