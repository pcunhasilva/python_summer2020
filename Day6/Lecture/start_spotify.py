## MOVE THIS FILE OFF GITHUB REPO BEFORE SYNCING!

## Register an app: https://developer.spotify.com/dashboard/login

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'YOUR ID'
client_secret = 'YOUR SECRET'

client_credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

