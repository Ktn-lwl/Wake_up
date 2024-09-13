"""
>   Learned a bit about using APIs. The code below opens Spotify on my laptop
    if it isn't open already.
>   I'm pretty wet behind the ears, so I censored some stuff just in case they're
    credentials that shouldn't be leaked. 
>   Censored stuff is in the form of capitalised strings spaced with underscores

>    UPDATE: Can wait till given time and start playback on my laptop
"""

import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from os import system

id = "APP_CLIENT_ID"
scp = "user-read-playback-state user-modify-playback-state"
secret = "CLIENT_SECRET"
redirect = "REDIRECT_URI"

my_laptop = "MY_LAPTOP_NAME"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = id, client_secret= secret,
                                               redirect_uri=redirect,
                                               scope=scp))

class Device:
    """
    This helps me handle devices as objects with 2 attributes: a name, and an
    ID
    """
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

def get_devices():
    """
    Makes a call to the spotify API to return data on all currently active 
    devices and then creates an instance of the Device class with it.
    Returns a dictionary containing currently active devices with the
    device names as keys.
    """
    devices = {}
    for device in sp.devices()["devices"]:
        devices[f"{device['name']}"] = Device(device["name"], device["id"])
    return devices

def get_time():
    """
    Returns a list with the current time (24hr clock) in the format: [hours, minutes]
    """
    return [time.localtime().tm_hour, time.localtime().tm_min]

def wait_till(exec_time):
    """
    Utilises the get_time() function defined above to keep the program in a loop
    until the provided time, exec_time, is reached
    """
    now = get_time()

    while f"{str(now[0]).rjust(2,'0')}:{str(now[1]).rjust(2,'0')}" != exec_time:
        system("cls")
        time.sleep(2)
        print("Not yet...")
        time.sleep(10)
        now = get_time()

active_devices = get_devices()

while my_laptop not in active_devices:
    """
    Check if my laptop is a currently active device, and if it isn't, opens Spotify
    via the command prompt
    """
    system("spotify")
    time.sleep(5)
    active_devices = get_devices()

wait_till("21:08")
system("cls")
print("GO TIME!")

sp.transfer_playback(active_devices[my_laptop].id)