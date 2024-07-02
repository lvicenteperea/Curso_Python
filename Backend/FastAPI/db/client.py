from pymongo import MongoClient

#Base de datos LOCAL
# db_client = MongoClient().local ## sin nada se conecta a mongo en local

# Bases de dato remota al mongoAtlas (mongodb+srv://test:test@atlascluster.iovqvw0.mongodb.net/)
db_client = MongoClient("mongodb+srv://test:test@atlascluster.iovqvw0.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"
                       ).test
