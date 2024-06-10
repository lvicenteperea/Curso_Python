#pip install "fastapi[all]"
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

#pip install "uvicorn[standard]"
#from typing import Union

router = APIRouter(prefix="/users", # ver documentación para ver como hay que hacer las llamadas
                   tags=["users"],  # es para que en la documentación separe los servicios de esta API
                   responses= {404: {"message": "No encontrado"}}
                  )
#uvicorn users:app --reload   --> que abre un servidor, normalmente en: http://127.0.0.1:8000
#******************************************************************************************************************

#Entidad User
'''
#-- con clases normales (luego se le han añadido mas cosas..):
class User():
    def __init__(self, nombre, apellido, email, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad

usuario = User("Usuario_32", "Apellido_12", "email_12@dominio.com", 221)

users_list = [User("Usuario_1", "Apellido_1", "email_1@dominio.com", 21),
              User("Usuario_2", "Apellido_2", "email_2@dominio.com", 22),
              User("Usuario_3", "Apellido_3", "email_3@dominio.com", 23),
              usuario]

# con BaseModel:
'''
class User(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: str
    edad: int

#Crear la variable que contiene toda nuestra lista registros de la entidad
users_list = [User(id=1, nombre="Usuario_1", apellido="Apellido_1", email="email_1@dominio.com", edad=21),
              User(id=2, nombre="Usuario_2", apellido="Apellido_2", email="email_2@dominio.com", edad=22),
              User(id=3, nombre="Usuario_3", apellido="Apellido_3", email="email_3@dominio.com", edad=23)]

#----- esta función es solo para simplificar código -----------
def busca_id_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0] 
    except:
        return {'error':'No se ha encontrado el usuario'}
#--------------------------------------------------------------


# ***********************************************************************************************
@router.get("/")
async def users():
    #return User(nombre="Usuario_1", apellido="Apellido_1", email="email_1@dominio.com", edad=21)
    return users_list

# ***********************************************************************************************
# formato query, es decir va como paramentros en la url: ..../id=1
@router.get("/user/")
async def user(id: int):
    return busca_id_user(id)

# ***********************************************************************************************
# formato path, es decir va en el PATH de la url: ..../1
@router.get("/user/{id}")
async def user(id: int):
    return busca_id_user(id)

@router.get("/usersname/{name}")
async def user(name: str):
    users = filter(lambda user: user.nombre == name, users_list)
    try:
        if users:
            return users
        else:
            return {"error":f"No se han encontrado usuarios con el nombre {name}"}
    except:
        return {"error":f"Error al buscar usuarios con el nombre {name}"}
# ***********************************************************************************************
@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(busca_id_user(user.id)) == User:
        raise HTTPException(status_code=204,detail=f"El usuario {user.nombre} ya existe")
        #return {"error":f"El usuario {user.nombre} ya existe"}

    users_list.append(user)
    return users_list

# ***********************************************************************************************
@router.put("/user/")
async def user(user: User):

    found = False
    for index, u in enumerate(users_list):
        if u.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error":f"El usuario {user.nombre} no existe"} 

    return users_list

# ***********************************************************************************************
@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, u in enumerate(users_list):
        if u.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error":f"El usuario {id} no existe"} 
    
    return users_list
