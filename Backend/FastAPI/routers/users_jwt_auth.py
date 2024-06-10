#pip install pyjwt
#pip install "passlib[bcrypt]"

from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from datetime import datetime, timedelta

#from BBDD import BBDD_users



ALGORITMO = "HS256"       # ALGORITHM
ACCESS_TOKEN_DURACION = 1 # ACCESS_TOKEN_DURATION
CLAVE_SECRET = "5b3846700bf8320a4b4b1dfe6a1f7b21ccf8f58e4f3019375f371fbb4e15361f" # se puede generar con "openssl rand -hex 32"

router = APIRouter(prefix="/users_jwt", # ver documentación para ver como hay que hacer las llamadas
                   tags=["users_jwtauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
cripto = CryptContext(schemes=["bcrypt"])

#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool  | None = False

class UserDB(User):
    password: str

class TokenRespuesta(BaseModel):
    acces_token: str
    token_type: str
    usuario: User  | None = None
    usuario_db: UserDB  | None = None

users_db = {
    "lvicente": {"username": "lvicente",
                    "full_name": "Luis Vicente",
                    "email": "lvicente@hangarxxi.com",
                    "disable": False,
                    "password": "$2a$12$jjRhXRlQ.XIDjniPDqJituayYjNbR91FVn1.AwHIxEqW2VVA69ZtS"  # "123456"
    },
    "lvicente2": {"username": "lvicente2",
                    "full_name": "Luis Vicente 2",
                    "email": "lvicente2@hangarxxi.com",
                    "disable": True,
                    "password": "$2a$12$VYB0VWvNJMlxC07CtE3jbuamePDLc8V0xnG.rzS4vindKL.xlef2."  #"654321"
    }
}

#**************************************************************************************************
def search_user_db(username: str = Depends(oauth2)):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


#**************************************************************************************************
async def auth_user(token: str = Depends(oauth2)):
    excepcion = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                              detail="Credenciales de autenticación inválidas",
                              headers={"WWW-Authenticate": "Bearer"})

    try:
        #username = jwt.decode(token, CLAVE_SECRET, algorithms=[ALGORITMO]).get("sub")
        header_sin_tokenizar = jwt.decode(token, CLAVE_SECRET, algorithms=[ALGORITMO])
        username = header_sin_tokenizar.get("sub")

        if username is None:
            raise excepcion

    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                              detail="Credenciales de autenticación inválidas3",
                              headers={"WWW-Authenticate": "Bearer"})

    print("MIO: " + username)
    return search_user(username)


#**************************************************************************************************
async def current_user(user: User = Depends(auth_user)):
    if user.disable:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Usuario inactivo")

    return user        
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************

@router.post("/login", response_model=TokenRespuesta)
async def login(form: OAuth2PasswordRequestForm = Depends()):

    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no es corecto")
    
    user = search_user_db(form.username)
    if not cripto.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="La contraseña no es corecta")

    access_token_expiracion = timedelta(minutes=ACCESS_TOKEN_DURACION) # para sumar un minuto a una fecha
    expira = datetime.now() + access_token_expiracion

    access_token = {"sub": user.username, 
                    "exp": expira,}

    token_respuesta = TokenRespuesta(acces_token = jwt.encode(access_token, 
                                                              CLAVE_SECRET, 
                                                              algorithm=ALGORITMO),
                                     token_type = "bearer",
                                     usuario_db = user_db # no se envia, lo he puesto por probar...
                                     )

    return token_respuesta # {"acces_token": jwt.encode(access_token, CLAVE_SECRET, algorithm=ALGORITMO), "token_type": "bearer"}


#**************************************************************************************************
@router.get("/me")
async def me(user: User = Depends(current_user)):
    return user



#**************************************************************************************************
'''
  { 
    "username": "username100", "full_name": "Luis Vicente", "email": "E@E.com", "password": "123456"
  }
'''
@router.post("/crea")
async def user(user: UserDB):
    user_db = users_db.get(user.username)

    if user_db:
        raise HTTPException(status_code=400, detail=f"El usuario {user.username} ya existe {user_db}")
    
    users_db[user.username] = {
                "username": user.username,
                "full_name": user.full_name, 
                "email": user.email, 
                "disable": False,
                "password": user.password #cripto.hash(CLAVE_SECRET, form.password)
    }
  
    return users_db
