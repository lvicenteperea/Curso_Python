# Se permite utilizar librerías que nos faciliten esta tarea.
from bs4 import BeautifulSoup
import requests

'''
#https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2318%20-%20WEB%20SCRAPING%20%5BDif%C3%ADcil%5D/python/Faliin.py
    * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
    * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
    *
    * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
    * del día 8. Mostrando hora e información de cada uno.
    * Ejemplo: "16:00 | Bienvenida"
    *
    * Se permite utilizar librerías que nos faciliten esta tarea.

    *Solución
        from bs4 import BeautifulSoup
        import requests

        blockquotes = BeautifulSoup(requests.get(
            "https://holamundo.day").content).find_all("blockquote")

        for blockquote in blockquotes[21:]:
            print(blockquote.text)
'''    

from bs4 import BeautifulSoup
import requests

blockquotes = BeautifulSoup(requests.get("https://holamundo.day"))
print("------------------")
print(blockquotes.text)
print("------------------")
agenda = blockquotes.content.find_all("blockquote")

for blockquote in blockquotes[21:]:
    print(blockquote.text)


'''
# Realizar la solicitud HTTP a la página web
url = "https://holamundo.day"
response = requests.get(url)

# Crear el objeto BeautifulSoup para analizar el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar la sección de la agenda del día 8

print("------------------")
print("   IMPRIMIR TEXT")
print("------------------")
print(soup.text)
print("------------------")

agenda = soup.find("div", {"class": "mayo"})
print("------------------")
print("   IMPRIMIR AGENDA")
print("------------------")
print(agenda)
print("------------------")
events = agenda.find_all("div", {"class": "event"})

# Imprimir la hora e información de cada evento del día 8
for event in events:
    time = event.find("span", {"class": "time"}).text.strip()
    info = event.find("span", {"class": "info"}).text.strip()
    print(f"{time} | {info}")
'''
