"""
module to create a layer of abstraction between main program and the spotipy api

input: one element from the 'albums'['items'] list

output: Album object
"""

from song import Song


class Album:
    
    def __init__(self, api_response):
        self.artists = api_response['artists']
