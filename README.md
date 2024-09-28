This is supposed to be a very annoying infinite alarm that plays if I snooze my final alarm for the morning
and some conditions aren't met. 
It uses the Spotify API via [spotipy](https://spotipy.readthedocs.io).

Spotipy can be installed with the command: `pip install spotipy --upgrade`
It can also be obtained from [its repo](https://github.com/spotipy-dev/spotipy) here on github.

- The main code is stored in *filtered_main.py*.

 Updates
 ---
  - Just added auto execution functionality with Windows via a batch file, *filtered_auto.bat*, that I scheduled to run every morning at 6:55 am using the Windows task scheduler exe.
