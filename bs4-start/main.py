from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movies = soup.find_all(class_="listicleItem_listicle-item__title__BfenH")
movies = movies[::-1]

for movie in movies:
    print(movie.getText())

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie.getText()}\n")