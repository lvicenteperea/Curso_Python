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

'''    
## MIO

from bs4 import BeautifulSoup
import requests

aux = requests.get("https://holamundo.day")
print(type(aux))
print(aux.text)
blockquotes = BeautifulSoup(aux.text)
print("------------------")
print(blockquotes.text)
print("------------------")
agenda = blockquotes.content.find_all("blockquote")

for blockquote in blockquotes[21:]:
    print(blockquote.text)



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

# ### IA #############

# Función para hacer scraping de eventos de un día específico
def scrape_events(url, day):
    # Enviar una solicitud GET a la página web
    response = requests.get(url)
    # Analizar el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    texto = soup.getText()

    # Buscar la sección que contiene la fecha
    date_section = soup.find(string=lambda text: day in texto)
    # Buscar el padre de la sección de la fecha que debería contener los eventos
    events_section = date_section.find_parent('section')
    

    # Buscar todos los eventos del día
    events = events_section.find_all(string=lambda text: '|' in text)
    
    # Extraer y devolver los eventos
    return [event.strip() for event in events]

# URL de la página de eventos
url = "https://holamundo.day"
# Día que quieres buscar
day_to_search = "7 de mayo"

# Scrapear eventos para "7 de mayo"
events = scrape_events(url, day_to_search)

# Imprimir los eventos
for event in events:
    print(event)