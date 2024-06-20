'''
ver el tiempo de cualquier ciudad del mundo
'''

from parametros import KEY
import requests

ciudad =  input("Introduce tu ciudad: ")
respuesta = requests.get(f"https://api.weatherapi.com/v1/current.json?key={KEY}&q={ciudad}")

json = respuesta.json()
print(json)