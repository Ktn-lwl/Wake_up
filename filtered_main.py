"""
>   I'm pretty wet behind the ears, so I censored some stuff just in case they're
    credentials that shouldn't be leaked. 
>   Censored stuff is in the form of capitalised strings spaced with underscores.
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
    This helps me handle devices as objects with 3 attributes: a name, and an
    ID, and whether or not it's active.
    """
    def __init__(self, name: str, id: str, is_active: bool):
        self.name = name
        self.id = id
        self.is_active = is_active

def get_devices():
    """
    Makes a call to the spotify API to return data on all currently active 
    devices and then creates an instance of the Device class with it.
    Returns a dictionary containing currently active devices with the
    device names as keys.
    """
    devices = {}
    for device in sp.devices()["devices"]:
        devices[f"{device['name']}"] = Device(device["name"], device["id"], device["is_active"])
    return devices

def get_time():
    """
    Returns a list with the current time (24hr clock) in the format: [hours, minutes]
    """
    return [time.localtime().tm_hour, time.localtime().tm_min]

def wait_till(exec_time: str):
    """
    Utilises the get_time() function defined above to keep the program in a loop
    until the provided time, exec_time, is reached. 
    exec_time is formatted as "XX:XX" in 24 hour time.
    """
    now = get_time()
    now = f"{str(now[0]).rjust(2,'0')}:{str(now[1]).rjust(2,'0')}"
    """
    format time tuple as "XX:XX" (don't want to get the time multiple times in the
    same statement because that might break stuff).
    """
    while now != exec_time:
        system("cls")
        time.sleep(2)
        print("Not yet...")
        time.sleep(10)
        now = get_time()
        now = f"{str(now[0]).rjust(2,'0')}:{str(now[1]).rjust(2,'0')}"

active_devices = get_devices()

while my_laptop not in active_devices:
    """
    Check if my laptop is a currently active device, and if it isn't, opens Spotify
    via the command prompt
    """
    system("spotify")
    time.sleep(5)
    active_devices = get_devices()

wait_till("07:05")
system("cls")
print("GO TIME!")

sp.transfer_playback(active_devices[my_laptop].id)

for i in range(5, 45, 2):
    """
    Keep checking until 7:45 whether I'm playing music on my laptop, 
    and forcing it to play if not
    """
    wait_till(f"07:{str(i).rjust(2,"0")}")
    active_devices = get_devices()
    
    if not active_devices[my_laptop].is_active:
        #laptop is inactive
        print("WAKE UP!!!")
        sp.transfer_playback(active_devices[my_laptop].id)
    
    elif not sp.current_user_playing_track():
        #the method above returns None if nothing is playing at the moment
        print("WAKE UP!!!")
        sp.transfer_playback(active_devices[my_laptop].id)

    elif not sp.current_user_playing_track()["is_playing"]:
        """
        the dictionary returned if there's a track in the player has a 
        boolean key 'is_playing'. In this case, activates if there IS a
        a song, but it's paused
        """
        print("WAKE UP!!!")
        sp.transfer_playback(active_devices[my_laptop].id)