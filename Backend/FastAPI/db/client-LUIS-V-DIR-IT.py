from pymongo import MongoClient

<<<<<<< HEAD
db_client = MongoClient() ## sin nada se conecta a mongo en local

=======
#Base de datos LOCAL
# db_client = MongoClient().local ## sin nada se conecta a mongo en local

# Bases de dato remota al mongoAtlas (mongodb+srv://test:test@atlascluster.iovqvw0.mongodb.net/)
db_client = MongoClient("mongodb+srv://test:test@atlascluster.iovqvw0.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"
                       ).test
>>>>>>> dc3361e6e5eaf2cf14ac4ac4df9c2c1789318d98
