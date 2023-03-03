#! /usr/bin/env python3

import sys
import json
import spotipy
import unittest
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

sys.path.insert(0, "..")
from classes.track import Track
from classes.user import User


class TestTrack(unittest.TestCase): 
    
    f = open('files/example_track_object.txt')
    example_track_object = json.loads(f.read())
    f.close()
    track = Track(example_track_object)

    load_dotenv()
    SCOPE = "user-library-read playlist-read-private"
    user = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    
    def test_get_id(self):
        self.assertEqual(self.track.get_id(), '0ntQJM78wzOLVeCUAW7Y45')

    def test_get_name(self):
        self.assertEqual(self.track.get_name(), 'Sex on Fire')

    def test_get_track_object(self):
        self.assertEqual(self.track.get_track_object(), self.example_track_object)

    def test_get_album(self):
        self.assertEqual(self.track.get_album(), 'Only By The Night')

    def test_get_artists(self):
        self.assertEqual(self.track.get_artists(), ['Kings of Leon'])

    def test_get_artist(self):
        self.assertEqual(self.track.get_artist(), 'Kings of Leon')

    def test_get_available_markets(self):
        self.assertEqual(self.track.get_available_markets(), ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 
            'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 
            'IS', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 
            'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 
            'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 
            'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 
            'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 
            'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 
            'PG', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 
            'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 
            'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 
            'VE', 'ET', 'XK']
        )

    def test_get_disc_number(self):
        self.assertEqual(self.track.get_disc_number(), 1)

    def test_get_duration_ms(self):
        self.assertEqual(self.track.get_duration_ms(), 203346)

    def test_is_explicit(self):
        self.assertEqual(self.track.is_explicit(), False)

    def test_get_external_ids(self):
        self.assertEqual(self.track.get_external_ids(), {'isrc': 'USRC10800300'})

    def test_get_external_urls(self):
        self.assertEqual(self.track.get_external_urls(), {'spotify': 'https://open.spotify.com/track/0ntQJM78wzOLVeCUAW7Y45'})

    def test_get_href(self):
        self.assertEqual(self.track.get_href(), 'https://api.spotify.com/v1/tracks/0ntQJM78wzOLVeCUAW7Y45')

    def test_is_local(self):
        self.assertEqual(self.track.is_local(), False)

    def test_get_popularity(self):
        self.assertEqual(self.track.get_popularity(), 78)

    def test_get_preview_url(self):
        self.assertEqual(self.track.get_preview_url(), 'https://p.scdn.co/mp3-preview/2f0905f484739399a749ec5605a09cb869211faf?cid=a11e01fd4f6145d8bcb032486a4390eb')

    def test_get_track_number(self):
        self.assertEqual(self.track.get_track_number(), 3)

    def test_get_type(self):
        self.assertEqual(self.track.get_type(), 'track')

    def test_get_uri(self):
        self.assertEqual(self.track.get_uri(), 'spotify:track:0ntQJM78wzOLVeCUAW7Y45')


    # turn this test off in Nov. 2023
    def test_is_saved(self):
        self.assertTrue(self.track.is_saved(self.user))

    def test_is_on_playlist(self):
        playlist_id = '1Kze4IV7B4E1hFPDAzHeZc'
        self.assertTrue(self.track.is_on_playlist(self.user, playlist_id))

    def test_is_on_a_playlist(self):
        self.assertTrue(self.track.is_on_a_playlist(self.user))

    def test_is_on_a_user_owned_playlist(self):
        self.assertTrue(self.track.is_on_a_user_owned_playlist(self.user))

if __name__ == "__main__":
    unittest.main()

