"""
module to create a layer of abstraction between main program and the spotipy api

input: a spotify track object

output: Track object
"""
from .user import User
import json

class Track:
    
    def __init__(self, track_object):
        self.id = track_object['id']
        self.name = track_object['name']
        self.track_object = track_object
        self.album_object = track_object['album']
        self.artists_object = track_object['artists']
        self.available_markets = track_object['available_markets']
        self.disc_number = track_object['disc_number']
        self.duration_ms = track_object['duration_ms']
        self.explicit = track_object['explicit']
        self.external_ids = track_object['external_ids']
        self.external_urls = track_object['external_urls']
        self.href = track_object['href']
        self.local = track_object['is_local']
        self.popularity = track_object['popularity']
        self.preview_url = track_object['preview_url']
        self.track_number = track_object['track_number']
        self.type = track_object['type']
        self.uri = track_object['uri']

    def __str__(self):
        return f"{self.get_name()}"


    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_track_object(self):
        return self.track_object

    def get_album_object(self):
        return self.album_object

    def get_album(self):
        return self.get_album_object()['name']

    def get_artists_object(self):
        return self.artists_object

    def get_artists(self):
        artists = [
            artist['name']
            for artist in self.get_artists_object()
        ]
        return artists

    def get_artist(self):
        return self.get_artists_object()[0]['name']

    def get_available_markets(self):
        return self.available_markets

    def get_disc_number(self):
        return self.disc_number

    def get_duration_ms(self):
        return self.duration_ms

    def is_explicit(self):
        return self.explicit

    def get_external_ids(self):
        return self.external_ids

    def get_external_urls(self):
        return self.external_urls

    def get_href(self):
        return self.href

    def is_local(self):
        return self.local

    def get_popularity(self):
        return self.popularity

    def get_preview_url(self):
        return self.preview_url

    def get_track_number(self):
        return self.track_number

    def get_type(self):
        return self.type

    def get_uri(self):
        return self.uri


    # returns True if track is saved by user sp
    def is_saved(self, user):
        return user.current_user_saved_tracks_contains(tracks=[self.get_id()])[0]

    # returns True if track is found on playlist
    def is_on_playlist(self, user, playlist_id):
        tracks = user.playlist_items(playlist_id, additional_types=('track',))
        while tracks:
            for track in tracks['items']:
                if track['track']['id'] == self.get_id():
                    return True
            if tracks['next']:
                tracks = user.next(tracks)
            else:
                tracks = None
        return False

    def is_on_a_playlist(self, user):
        playlists = user.current_user_playlists()
        while playlists:
            for playlist in playlists['items']:
                playlist_id = playlist['id']
                if self.is_on_playlist(user, playlist_id):
                    return True
            if playlists['next']:
                playlists = user.next(playlists)
            else:
                playlists = None
        return False

    def is_on_a_user_owned_playlist(self, user):
        playlists = user.current_user_playlists()
        while playlists:
            for playlist in playlists['items']:
                playlist_id = playlist['id']
                if playlist['owner']['id'] == user.me()['id'] and self.is_on_playlist(user, playlist_id):
                    return True
            if playlists['next']:
                playlists = user.sp.next(playlists)
            else:
                playlists = None
        return False


