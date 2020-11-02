import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secrets import client_id, client_secret, lifxtoken
from LFXControl import LIFXController
import time


if __name__ == "__main__":
    lifx = LIFXController(lifxtoken)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri='http://localhost:8080',
                                                   scope='user-read-playback-state'
                                                   ))
    error = False
    while(error != True):
        try:
            if sp.currently_playing()['is_playing']:
                print("Song is playing")
                lifx.changeColor('lamp', 'red')

            else:
                lifx.changeColor('lamp', 'green')
                print("song not playing")
        except:
            error = True
        time.sleep(5)
