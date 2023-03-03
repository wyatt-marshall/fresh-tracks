#! /usr/bin/env python3

"""
multithreading test

2023-03-03
"""

import random
import threading
from queue import Queue
import json
import time
from time import sleep
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from classes.track import Track
from classes.user import User


load_dotenv()

SCOPE = "user-library-read playlist-read-private user-modify-playback-state"

user = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))


# returns list of all track ids on a playlist
def get_track_ids_from_playlist(user, playlist_id, output_queue):
    track_ids = []
    tracks = user.playlist_items(playlist_id, additional_types=('track',))
    while tracks:
        for track in tracks['items']:
            track_ids.append(track['track']['id'])
        if tracks['next']:
            tracks = user.next(tracks)
        else:
            tracks = None
    #return track_ids
    output_queue.put(track_ids)

def get_user_saved_tracks_ids(user):
    track_ids = []
    saved_tracks = user.current_user_saved_tracks(limit=50)
    while saved_tracks:
        for track in saved_tracks['items']:
            track_ids.append(track['track']['id'])
        if saved_tracks['next']:
            saved_tracks = user.next(saved_tracks)
        else:
            saved_tracks = None
    return track_ids

# returns list of track ids for all tracks on all user owned playlists
def get_all_user_owned_tracks(user):
    track_ids = []
    playlists = user.current_user_playlists()
    while playlists:
        for playlist in playlists['items']:
            if playlist['owner']['id'] == user.me()['id']:
                playlist_id = playlist['id']
                track_ids.extend(get_track_ids_from_playlist(user, playlist_id))
        if playlists['next']:
            playlists = user.next(playlists)
        else:
            playlists = None
    track_ids.extend(get_user_saved_tracks_ids(user))
    return track_ids

def get_all_user_owned_playlists_ids(user):
    all_playlist_ids = []
    playlists = user.current_user_playlists()
    while playlists:
        for playlist in playlists['items']:
            if playlist['owner']['id'] == user.me()['id']:
                all_playlist_ids.append(playlist['id'])
        if playlists['next']:
            playlists = user.next(playlists)
        else:
            playlists = None
    return all_playlist_ids


def process_id(idx, output_queue):
    id_ids = []
    sleep(3)
    for i in range(10):
        id_ids.append(random.randint(1, 100))
    #return id_ids
    output_queue.put(id_ids)

#ids = [1, 2, 3, 4, 5]
#threads = []
#output_queue = Queue()
#for idx in ids:
    #t = threading.Thread(target=process_id, args=(idx, output_queue))
    #threads.append(t)
    #t.start()

#for t in threads:
    #t.join()

#all_ids = []
#while not output_queue.empty():
    #all_ids.extend(output_queue.get())

#print(all_ids)
#print(len(all_ids))
#exit()


playlist_ids = get_all_user_owned_playlists_ids(user)
threads = []
output_queue = Queue()
for playlist in playlist_ids:
    t = threading.Thread(target=get_track_ids_from_playlist, args=(user, playlist, output_queue))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

all_ids = []
while not output_queue.empty():
    all_ids.extend(output_queue.get())
all_ids = list(set(all_ids))
print(len(all_ids))
    
exit()


all_user_owned_tracks = get_all_user_owned_tracks(user)
all_user_owned_tracks = list(set(all_user_owned_tracks))
print(len(all_user_owned_tracks))

