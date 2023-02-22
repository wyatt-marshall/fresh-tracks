"""
module to create a layer of abstraction between main program and the spotipy api

input: one element from the 'tracks'['items'] list

output: Song object
"""
from user import User
import json

class Track:
    
    def __init__(self, api_response):
        self.album = api_response['album']
        self.artists = api_response['artists']
        self.available_markets = api_response['available_markets']
        self.disc_number = api_response['disc_number']
        self.duration_ms = api_response['duration_ms']
        self.explicit = api_response['explicit']
        self.external_ids = api_response['external_ids']
        self.external_urls = api_response['external_urls']
        self.href = api_response['href']
        self.id = api_response['id']
        self.is_local = api_response['is_local']
        self.name = api_response['name']
        self.popularity = api_response['popularity']
        self.preview_url = api_response['preview_url']
        self.track_number = api_response['track_number']
        self.type = api_response['type']
        self.uri = api_response['uri']


    def __str__(self):
        return f"{self.name}\n{self.artists[0]['name']}\n{self.album['name']}"


    def get_track_id(self):
        track_id = self.id
        return track_id

    def get_track_name(self):
        name = self.name
        return name

    def get_artist(self):
        artist = self.artists[0]["name"]
        return artist

    # returns True if track is saved by user sp
    def is_saved(self, user):
        saved = user.sp.current_user_saved_tracks_contains(tracks=[self.id])[0]
        return saved

    # returns True if track is found on playlist
    def is_track_on_playlist(self, user, playlist_id):
        playlist_tracks = user.sp.playlist_tracks(playlist_id)
        while playlist_tracks:
            for playlist_track in playlist_tracks['items']:
                if playlist_track['track']['id'] == self.get_track_id():
                    return True
            if playlist_tracks['next']:
                playlist_tracks = user.sp.next(playlist_tracks)
            else:
                playlist_tracks = None
        return False

    def is_on_a_playlist(self, user):
        playlists = user.sp.current_user_playlists()
        while playlists:
            for playlist in playlists['items']:
                playlist_id = playlist['id']
                if self.is_track_on_playlist(user, playlist_id):
                    return True
            if playlists['next']:
                playlists = user.sp.next(playlists)
            else:
                playlists = None
        return False

