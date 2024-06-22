#pip install "fastapi[all]"
from fastapi import APIRouter, HTTPException, status
from db.modelos.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

#pip install "uvicorn[standard]"
#from typing import Union
#uvicorn users:app --reload   --> que abre un servidor, normalmente en: http://127.0.0.1:8000
#******************************************************************************************************************

router = APIRouter(prefix="/userdb", # ver documentación para ver como hay que hacer las llamadas
                   tags=["userdb"],  # es para que en la documentación separe los servicios de esta API
                   responses= {404: {"message": "No encontrado"}}
                  )


''' -----------------------------------------
    @ Busqueda por ID
    # Ejemplo de uso:
        usuario_encontrado = busca_user_por_id(id)
----------------------------------------- '''
def busca_user_por_id(id: str):
    try:
        user = db_client.local.users.find_one({"_id": ObjectId(id)})
        if user:
            return User(**user_schema(user))
        else:
            return {'error': f"No se ha encontrado el usuario con ID = {id}"}
    except:
        return {'error': f'Error al buscar el usuario {id}'}

'''-----------------------------------------
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
# Listado de todos los usuarios
# ***********************************************************************************************
@router.get("/", response_model=list[User])
async def users():
    """
    saca un listado con todos los usuarios

    Args:
        No hay

    Returns:
        list: lista tipo User de la BBDD
    """
    return users_schema(db_client.local.users.find())

# ***********************************************************************************************
# formato query, es decir va como paramentros en la url: ..../id=1
# ***********************************************************************************************
@router.get("/", response_model=User)
async def user(id: str):
    return busca_user_por_id(id)

# ***********************************************************************************************
# formato path, es decir va en el PATH de la url: ..../1
# ***********************************************************************************************
@router.get("/{id}", response_model=User)
async def user(id: str):
    return busca_user_por_id(id)

# ***********************************************************************************************
@router.get("/usersname/{name}")
async def user(name: str):
    users = filter(lambda user: user.nombre == name, users_list)
    try:
        if users:
            return users
        else:
            return {"error": f"No se han encontrado usuarios con el nombre {name}"}
    except:
        return {"error": f"Error al buscar usuarios con el nombre {name}"}

# ***********************************************************************************************
# Insertamos usuarios cuidando de que no se repita el nombre
# ***********************************************************************************************
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
@router.post("/", response_model=User, status_code=status.HTTP_202_ACCEPTED)
async def user(user: User):
    """
    Inserta un usuario en BBDD sin no existe otro con el mismo nombre o con el mismo email
    
    Args:
        user: tipo User de la BBDD
    
    Returns:
        user: tipo User de la BBDD

    Raises:
        HTTPException:
            - status_code 204: Si el usuario ya existe en la base de datos.
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
# ACTUALIZACION
# ***********************************************************************************************
@router.put("/", status_code=status.HTTP_201_CREATED)
async def user(user: User):
    """
    ACTUALIZA un usuario en BBDD 
    
    Args:
        user: De tipo User de BBDD
    
    Returns:
        user si todo Ok
        Error, diccionario
    """

    user_dict = dict(user)
    del user_dict["id"] # me lo cargo del diccionario porque este campo no se actualiza

    encontrado = busca_user_por_id(user.id)
    print("-----------------------")
    print(type(encontrado))
    print(encontrado)
    print("-----------------------")

    if type(encontrado) == User: # es diccionario porque es el texto del error
        try:
            db_client.local.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
        except:
            return {"Error:": f"No se ha actualizado el usuario {user.id} - {user.nombre}"}
    else:
        return {"Error:": f"el usuario {user.id} - {user.nombre} no existe"}

    return busca_user_por_id(user.id)

# ***********************************************************************************************
# ***********************************************************************************************
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    """
    BORRA un usuario en BBDD 
    
    Args:
        user: ID
    
    Returns:
        Nada

    Raises:
        HTTPException:
            - status_code 204: Si el usuario ya existe en la base de datos.
    """
    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error":f"El usuario {id} no existe"} 
    
