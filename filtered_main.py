"""
>   Learned a bit about using APIs. The code below opens Spotify on my laptop
    if it isn't open already.
>   I'm pretty green behind the ears, so I censored some stuff just in case they're
    credentials that shouldn't be leaked. 
>   Censored stuff is in the form of capitalised strings spaced with underscores

>    UPDATE: Transfers playback to my laptop and starts playing music
"""

import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from os import system

id = "APP_CLIENT_ID"
read_scp = "user-read-playback-state"
write_scp = "user-modify-playback-state"
secret = "CLIENT_SECRET"
redirect = "REDIRECT_URI"

my_laptop = "MY_LAPTOP_NAME"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = id, client_secret= secret,
                                               redirect_uri=redirect,
                                               scope=read_scp))

class Device:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

def get_devices():
    devices = {}
    for device in sp.devices()["devices"]:
        devices[f"{device['name']}"] = Device(device["name"], device["id"])
    return devices

active_devices = get_devices()

while my_laptop not in active_devices.keys():
    system("spotify")
    time.sleep(5)
    active_devices = get_devices()

print("DONE!")

sp.auth_manager.scope = write_scp

sp.transfer_playback(active_devices[my_laptop].id)