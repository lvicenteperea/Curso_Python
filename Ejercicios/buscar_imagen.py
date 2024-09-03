import requests
from PIL import Image
from io import BytesIO

def buscar_imagen(query):
    api_key = 'tu_api_key_de_unsplash'  # Sustituye con tu API Key de Unsplash
    url = f'https://api.unsplash.com/search/photos?query={query}&client_id={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['results']:
        image_url = data['results'][0]['urls']['regular']
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()
    else:
        print("No se encontraron imágenes.")

query = input("Ingresa la palabra clave para buscar imágenes: ")
buscar_imagen(query)
