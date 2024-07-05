import requests


print("Listando los clientes mediante API...\n")

respuesta = requests.get("http://127.0.0.1:8000/clientedb/")

json = respuesta.json()
print(json)