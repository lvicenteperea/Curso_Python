from pymongo import MongoClient

'''
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
'''

#Base de datos LOCAL
# db_client = MongoClient().local ## sin nada se conecta a mongo en local

# Bases de dato remota al mongoAtlas (mongodb+srv://test:test@atlascluster.iovqvw0.mongodb.net/)
db_client = MongoClient("mongodb+srv://test:test@atlascluster.iovqvw0.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"
                       ).test