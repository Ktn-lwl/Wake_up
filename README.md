This is ~~supposed to be~~ a very annoying ~~infinite~~ recurring alarm that plays if I snooze my final alarm for the morning
and some conditions aren't met. 
It uses the Spotify API via [spotipy](https://spotipy.readthedocs.io)[^1].

Spotipy can be installed with the command: `pip install spotipy --upgrade`
It can also be obtained from [its repo](https://github.com/spotipy-dev/spotipy) here on github.

- The main code is stored in *filtered_main.py*.

Some background info:
---
- I linked my phone alarm to my Spotify
- I wake up to certain songs daily
- My warning alarm is at 6:30 am, my final is by 7:00 am.
- Everyday, when I wake up, I send my alarm song to play on my laptop - which is always open and plugged in on my desk in the morning from previous night - at full blast. __This only happens when I've fully woken up.__
- I'm only human, so I sometimes snooze _all_ my alarms including the final one.


Target Functionality
---
 Since I blast music on my laptop in the morning, the code should:
 
- [x] Check if I've ~~played a song at full blast~~ opened Spotify on my laptop and am playing music by 7:05 am.
       
If I haven't:
1. [ ] Turn my laptop volume all the way up[^2]
2. [x] Switch my Spotify playback device (my phone from the alarms) to my laptop[^3]
3. [x] Play some music[^4].
       
If I'm still really groggy and pause the music from my phone:

- [x] resume playback with a 2 minute grace period until I close the app, ~~or - for something more interesting - complete a challenge.~~

Updates
---
##### Compromised some keys
- **Issue** : Accidentally leaked some files with secret credentials in a previous commit.
- **Fix** : Force reversed to a previous commit. Destroyed leaked credentials and replaced them with new ones.
##### Fixed auto-execution bug
- **Issue** : The code when executed via the filtered_auto.bat file using the task scheduler utility on Windows occasionally halted execution to ask for an Authentication link from the browser page opened. This should only happen the first time the code is executed and generate a .cache file to be used for subsequent executions.
- **Fix** : Edited filtered_auto.bat to change the working directory before the code is executed.

What's Next
---
I need to figure out:
- how to adjust the system volume automatically
- how the whole OAuth2 credential thingy works and perhaps automate the whole fetching process so other people can use my code since I'm pretty much done :)

[^1]: I'll eventually learn how to use the requests module, and maybe update this to be wholly my own.
[^2]: It seems I will need to either find a way to do this via a batchfile, i.e (finally get round to properly learning Powershell), or with Python or C++ using the windows API. In any case, some studying is requisite, so I'd better get cracking :-)
[^3]: I might make it playback from my phone depending on the effectiveness. So I'll get an annoying infinite alarm until I terminate the code.
[^4]: ~~I'm considering using Of Monsters and Men's _'Visitor'_, but I might just make it pick a random song from my playlist.~~ Random music is fine to break monotony.
