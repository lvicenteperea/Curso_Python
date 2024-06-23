import requests
from bs4 import BeautifulSoup ## pip install beautifulsoup4


blockquotes = BeautifulSoup(requests.get(
    "https://holamundo.day").content).find_all("blockquote")

for blockquote in blockquotes[21:]:
    print(blockquote.text)