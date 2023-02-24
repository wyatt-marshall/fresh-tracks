"""
module to create a layer of abstraction between main program and the spotipy api

input: a spotipy playlist object

output: Playlist object
"""


class Playlist:
    
    def __init__(self, playlist):
        self.playlist = playlist

    def __str__(self):
        return self.playlist['name']

    
    def get_playlist_id(self):
        return self.playlist['id']

    def get_playlist_owner_id(self):
        return self.playlist['owner']['id']
