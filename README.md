This is supposed to be a very annoying infinite alarm that plays if I snooze my final alarm for the morning
and some conditions aren't met. 
It uses the Spotify API via [spotipy](https://spotipy.readthedocs.io).

Spotipy can be installed with the command: `pip install spotipy --upgrade`
It can also be obtained from [its repo](https://github.com/spotipy-dev/spotipy) here on github.

- The main code is stored in *filtered_main.py*.

Some background info:
---
>- I linked my phone alarm to my Spotify
>- I wake up to certain songs daily
>- My warning alarm is at 6:30 am, my final is by 7:00 am.
>- Everyday, when I wake up, I send my alarm song to play on my laptop - which is always open and plugged in on my desk in the morning from previous night - at full blast. __This only happens when I've fully woken up.__
>- I'm only human, so I sometimes snooze _all_ my alarms including the final one.


Target Functionality
---
> Since I blast music on my laptop in the morning, the code should:
> 
> - [ ] Check If I've played a song at full blast by 7:05 am.
>       
>  If I haven't:
>  1. [ ] Turn my laptop volume all the way up
>  2. [-] Switch my Spotify playback device (my phone from the alarms) to my laptop[^1]
>  3. [-] Play some music[^2].
>         
>   If I'm still really groggy and pause the music from my phone:
>   
>   - [-] resume playback with a 2 minute grace period until I close the app, or - for something more interesting - complete a challenge.

[^1]:  I might make it playback from my phone depending on the effectiveness. So I'll get an annoying infinite alarm until I terminate the code.
[^2]:  I'm considering using Of Monsters and Men's _'Visitor'_, but I might just make it pick a random song from my playlist.

 Updates
 ---
  - Just added auto execution functionality with Windows via a batch file, *filtered_auto.bat*, that I scheduled to run every morning at 6:55 am using the Windows task scheduler exe.
