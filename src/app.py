import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

import os

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

artist_id = '6fOMl44jA4Sp5b9PpYCkzz'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret))
results = spotify.artist_top_tracks(artist_id)

songs=[]
popularity=[]
duration=[]

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    songs.append(track['name'])
    popularity.append(track['popularity'])
    duration.append(track['duration_ms']/(1000*60)%60)

df = pd.DataFrame()

df['songs'] = songs
df['popularity'] = popularity
df['duration'] = duration

df_ascending = df.sort_values(by='popularity', ascending=False)
df_ascending

df_ascending.head(3)

Popularity_duration_tracks = df.plot.scatter(x='duration',
                      y='popularity',
                      c='DarkBlue'
                      )
