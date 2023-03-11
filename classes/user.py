"""
module to create a layer of abstraction between main program and the spotipy api

input: a spotipy user object

output: User object
"""
import random
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

    # returns list of track ids for all songs that are on user owned playlists
    def get_all_user_owned_tracks(self):
        playlists = self.user.current_user_playlists()
        all_track_ids = []
        while playlists:
            for playlist in playlists['items']:
                playlist = Playlist(playlist)
                playlist_owner_id = playlist.get_playlist_owner_id()
                if playlist_owner_id == self.get_user_id():
                    playlist_id = playlist.get_playlist_id()
                    all_track_ids.extend(self.get_track_ids_from_playlist(playlist_id))
            if playlists['next']:
                playlists = self.sp.next(playlists)
            else:
                playlists = None
        return all_track_ids

    def get_user_owned_playlists(self):
        all_playlists = []
        playlists = self.user.current_user_playlists()
        while playlists:
            for playlist in playlists['items']:
                if playlist['owner']['id'] == self.get_id():
                    all_playlists.append(playlist)
            if playlists['next']:
                playlists = self.next(playlists)
            else:
                playlists = None
        return all_playlists

    def get_id_from_playlist(self, playlist):
        return playlist['id']
    
    def get_ids_from_playlists(self, playlists):
        return list(map(lambda x: self.get_id_from_playlist(x), playlists))

    def get_all_user_owned_playlist_ids(self):
        all_playlists = self.get_user_owned_playlists()
        return self.get_ids_from_playlists(all_playlists)

    def search_track(self):
        track_name = input("Track: ")
        response = self.user.search(track_name, type='track')
        while response:
            for track in response['tracks']['items']:
                print(track['name'])
                print(track['artists'][0]['name'])
                print(track['album']['name'])
                print('')
                select = input("y or n? ")
                if select == 'y':
                    return track
                else:
                    pass
            if response['tracks']['next']:
                response = self.user.next(response['tracks'])
            else:
                response = None
        print("Track not found.")
        exit(1)

    def get_recommendations(self, track_id):
        recs = self.user.recommendations(seed_tracks=[track_id], limit=100, country='US')
        return recs

    #def get_new_recs(self, seed_id, track_ids, num_recs):
        #recs = self.get_recommendations(seed_id)
        #new_recs = []
        #while recs:
            #for rec in recs['tracks']:
                #if len(new_recs) == num_recs:
                    #return new_recs
                #if rec['id'] in track_ids:
                    #pass
                #else:
                    #new_recs.append(rec)
            #recs = self.get_recommendations(seed_id)

    def get_some_new_recs(self, seed_id, track_ids, num_recs, percent):
        recs = self.get_recommendations(seed_id)
        some_new_recs = []
        while recs:
            for rec in recs['tracks']:
                if len(some_new_recs) == num_recs:
                    return some_new_recs
                if rec['id'] in track_ids:
                    chance = percent * 100
                    num = random.randint(1, 100)
                    if chance > num:
                        some_new_recs.append(rec)
                else:
                    some_new_recs.append(rec)
            recs = self.get_recommendations(seed_id)



    def add_to_queue(self, track_list):
        for track in track_list:
            self.user.add_to_queue(track['id'])


                


