import requests
from bs4 import BeautifulSoup

def scraping_web(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for titulo in soup.find_all('h1'):
        print(titulo.text)

url = input("Ingresa la URL para hacer scraping: ")
scraping_web(url)
