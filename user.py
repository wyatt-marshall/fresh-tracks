"""
module to create a layer of abstraction between main program and the spotipy api

input: a spotipy user object

output: User object
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class User:
    
    def __init__(self, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, SCOPE):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                              client_secret=SPOTIPY_CLIENT_SECRET,
                                                              redirect_uri=SPOTIPY_REDIRECT_URI,
                                                              scope=SCOPE))
        self.display_name = self.sp.me()['display_name']

    def __str__(self):
        display_name = self.display_name
        return display_name

