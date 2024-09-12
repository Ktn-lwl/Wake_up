"""
Still learning to use the Spotify API, but I did get some proof of concept
that I can make my code wait until a certain time to do something
"""

import time

def get_time():
    return [time.localtime().tm_hour, time.localtime().tm_min]

while True:
    if get_time()[1] == 27:
        print("There")
        time.sleep(5)
        break
    else:
        print("not yet")
        time.sleep(5)