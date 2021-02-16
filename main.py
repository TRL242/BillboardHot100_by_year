import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# CLIENT_ID = "8329221ed7b744f1b3239a9d34c0b105"
# CLIENT_SECRET = "3793bbf3b81a4508a6892be8e3d6c1cd"
print(os.environ.get('CLIENT_ID'))
print(os.environ.get('CLIENT_SECRET'))

# date = input("What year in the past are you looking to go to? YYYY-MM-DD: \n")
#
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
#
# soup = BeautifulSoup(response.text, "html.parser")
# # print(soup)
# song_names_spans = soup.find_all("span", class_="chart-element__information__song")
# song_names = [song.getText() for song in song_names_spans]
# #print(song_names)
#
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=YOUR UNIQUE CLIENT ID,
#         client_secret=YOUR UNIQUE CLIENT SECRET,
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user()["id"]
for i, j in os.environ.items():
    print(i, j)
    #print(os.environ['CLIENT_ID'])
print(usr/bin/env/CLIENT_ID)