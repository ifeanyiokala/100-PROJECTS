from bs4 import BeautifulSoup
import requests


date = input("What year would you like to travel to ? Type the date in this format YYYY-MM-DD:")



response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

test = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

# print(test.text)

no_plus_minus = str.maketrans("", "", "\t\n")
name =[head.getText() for head in test]
song_names=[s.translate(no_plus_minus) for s in name]
# print(name)
# print(test.getText())




# <h3 id="title-of-a-story" class="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only">

	
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com" ,
        client_id="f6fb3838a5884ab8bc32b96d16a9f39a",
        client_secret="344b1ba1899749d481880b2eb288614a",
        show_dialog=True,
        cache_path="token.txt"

    )
)
user_id = sp.current_user()["id"]
# user_id = sp.current_user()["id"]
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# song_names= ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")



playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
# print(result)


	# username_ID = go1fawbeq7tau2bxlu0hxhrpk
    
# playlists = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100.")

# sp.playlist_add_items(playlist_id=playlists["id"], items=song_uris)
# print(sp)
	
# Client ID = f6fb3838a5884ab8bc32b96d16a9f39a

# Client Secret = 344b1ba1899749d481880b2eb288614a


# OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'

# OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'


# __init__(client_id="f6fb3838a5884ab8bc32b96d16a9f39a", client_secret="344b1ba1899749d481880b2eb288614a", redirect_uri="http://myplaylist.com/callback/", state=None, scope=None, cache_path=None, username=None, proxies=None, show_dialog=False, requests_session=True, requests_timeout=None)


	
	
		
	