"""
>   Learned a bit about using APIs. The code below opens Spotify on my laptop
    if it isn't open already.
>   I'm pretty green behind the ears, so I censored some stuff just in case they're
    credentials that shouldn't be leaked. 
>   Censored stuff is in the form of capitalised strings spaced with underscores

"""

import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from os import system

id = "APP_CLIENT_ID"
scp = "user-read-playback-state"
secret = "CLIENT_SECRET"
redirect = "REDIRECT_URI"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = id, client_secret= secret,
                                               redirect_uri=redirect,
                                               scope=scp))

device_names = [device["name"] for device in sp.devices()["devices"]]

my_laptop = "MY_LAPTOP_NAME"

while my_laptop not in device_names:
    system("spotify")
    time.sleep(5)
    device_names = [device["name"] for device in sp.devices()["devices"]]

print("DONE!")