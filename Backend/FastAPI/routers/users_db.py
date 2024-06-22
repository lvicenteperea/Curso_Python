#pip install "fastapi[all]"
from fastapi import APIRouter, HTTPException, status
from db.modelos.user import User
from db.client import db_client
from db.schemas.user import user_schema

#pip install "uvicorn[standard]"
#from typing import Union
#uvicorn users:app --reload   --> que abre un servidor, normalmente en: http://127.0.0.1:8000
#******************************************************************************************************************

router = APIRouter(prefix="/userdb", # ver documentación para ver como hay que hacer las llamadas
                   tags=["userdb"],  # es para que en la documentación separe los servicios de esta API
                   responses= {404: {"message": "No encontrado"}}
                  )

#Crear la variable que contiene toda nuestra lista registros de la entidad
users_list = []


#----- esta función es solo para simplificar código -----------
def busca_id_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0] 
    except:
        return {'error':'No se ha encontrado el usuario'}
#--------------------------------------------------------------
''' -----------------------------------------
    @ Busqueda por cualquier campo
    # Ejemplo de uso:
        nombre_a_buscar = "Juan"
        usuario_encontrado = busca_user_por_campo("nombre", nombre_a_buscar)
----------------------------------------- '''
def busca_user_por_campo(campo: str, valor: str):
    try:
        query = {campo: valor}
        user = db_client.local.users.find_one(query)
        if user:
            print(f"Usuario de BBDD {user}")
            return User(**user_schema(user))
        else:
            return {'error': f"No se ha encontrado el usuario con {campo} igual a {valor}"}
    except:
        return {'error': 'Error al buscar el usuario'}
#--------------------------------------------------------------
''' -----------------------------------------
    @ Busqueda por VARIOS CAMPOS. si encuentra por cualquiera de ellos, retorna el usuario
    # Ejemplo de uso:
        campos_a_buscar = {"nombre": "Juan", "edad": 30}
        usuario_encontrado = busca_user_por_campos(campos_a_buscar)
----------------------------------------- '''
def busca_user_por_campos(campos_valores: dict):
    try:
        query = {"$or": []}
        for campo, valor in campos_valores.items():
            query["$or"].append({campo: valor})
        
        user = db_client.local.users.find_one(query)
        if user:
            print(f"Usuario de BBDD {user}")
            return User(**user_schema(user))
        else:
            return {'error': 'No se ha encontrado el usuario con los campos proporcionados'}
    except:
        return {'error': 'Error al buscar el usuario'}


# ***********************************************************************************************
@router.get("/")
async def users():
    return users_list

# ***********************************************************************************************
# formato query, es decir va como paramentros en la url: ..../id=1
@router.get("/")
async def user(id: int):
    return busca_id_user(id)

# ***********************************************************************************************
# formato path, es decir va en el PATH de la url: ..../1
@router.get("/{id}")
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
''' 
    @ Insertamos usuarios cuidando de que no se repita el nombre
'''
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    """
    Inserta un usuario en BBDD sin no existe otro con el mismo nombre o con el mismo email
    
    Args:
        user: tipo User de la BBDD
    
    Returns:
        user: tipo User de la BBDD
    """
    #busco si existe el usuario por NOMBRE o EMAIL
    campos_a_buscar = {"nombre": user.nombre, "email": user.email}
    if type(busca_user_por_campos(campos_a_buscar)) == User:
       raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"El usuario {user.nombre} - {user.email} ya existe")

    
    user_dict = dict(user)
    del user_dict["id"] # me lo cargo del diccionario porque es una inserción y no puede ir este campo, ya que se autogenera

    #    (creamos el registro en BB)                (recuperamos el id)
    id = db_client.local.users.insert_one(user_dict).inserted_id

    # Recuperamos el usuario de BBDD y con user_schema, lo transformamos en un user JSON
    new_user = user_schema(db_client.local.users.find_one({"_id": id})) 

    return User(**new_user)

# ***********************************************************************************************
@router.put("/")
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
@router.delete("/{id}")
async def user(id: int):
    found = False
    for index, u in enumerate(users_list):
        if u.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error":f"El usuario {id} no existe"} 
    
    return users_list
