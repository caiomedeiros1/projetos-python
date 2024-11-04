from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/instant_pot/")
soup = BeautifulSoup(response.text, "html.parser")

whole = soup.find(class_="a-price-whole").getText()
fraction = soup.find(class_="a-price-fraction").getText()

print(whole + fraction)