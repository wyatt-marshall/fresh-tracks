#! /usr/bin/env python3

import os
import sys
#import json
import unittest
from dotenv import load_dotenv

sys.path.insert(0, "..")
from classes.user import User


class TestUser(unittest.TestCase):
    load_dotenv()
    SCOPE = "user-library-read playlist-read-private"
    user = User(SCOPE)

    

    def test_get_id(self):
        self.assertEqual(self.user.get_id(), 'wywymarsh')

    def test_get_display_name(self):
        self.assertEqual(self.user.get_display_name(), 'wywymarsh')

    def test_get_external_urls(self):
        self.assertEqual(self.user.get_external_urls(), {"spotify": "https://open.spotify.com/user/wywymarsh"})

    def test_get_follower_count(self):
        self.assertEqual(self.user.get_follower_count(), 34)

    def test_get_href(self):
        self.assertEqual(self.user.get_href(), 'https://api.spotify.com/v1/users/wywymarsh')
    
    def test_get_uri(self):
        self.assertEqual(self.user.get_uri(), 'spotify:user:wywymarsh')



if __name__ == "__main__":
    unittest.main()

