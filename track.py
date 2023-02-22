"""
module to create a layer of abstraction between main program and the spotipy api

input: one element from the 'tracks'['items'] list

output: Song object
"""


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



