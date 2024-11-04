from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id="5a422f7bda6b4843939416f05f879bf0",
        client_secret="e5ee1d38e40f49b38507d5c1ce1f9342",
        show_dialog=True,
        cache_path="token.txt",
        username="caiomedeiros", 
    )
)
user_id = sp.current_user()["id"]

#date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

date = "2000-08-12"
response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

songs = soup.select("li ul li h3")
songs_formatted = [song.getText().strip() for song in songs]

song_uris = []
year = date.split("-")[0]
for song in songs_formatted:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
