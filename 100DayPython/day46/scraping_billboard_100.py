import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime

date_string = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD:')
date_format = '%Y-%m-%d'
try:
    date = datetime.datetime.strptime(date_string, date_format)
except ValueError:
    raise ValueError('Your date is incorrect')

year = date.year

endpoint = f'https://www.billboard.com/charts/hot-100/{date_string}'
response = requests.get(url = endpoint)
soup = BeautifulSoup(response.text, 'html.parser')
song_elements = soup.select('ul li h3.c-title')
song_titles = []
for element in song_elements:
    if element.string != None:
        song_titles.append(element.string.strip())


spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
song_uris = []
for song_title in song_titles:
    search = spotify.search(f'track:{song_title} year:{year}', limit=10, offset=0, type='track', market=None)
    try:
        uri = search["tracks"]["items"][0]["uri"]
        print(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song_title} doesn't exist in Spotify. Skipped.")

print(song_uris)

