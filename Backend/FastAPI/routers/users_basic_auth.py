from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/users_basic", # ver documentación para ver como hay que hacer las llamadas
                   tags=["users_basic_auth"],  # es para que en la documentación separe los servicios de esta API
                   responses= {404: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool

class UserDB(User): 
    password: str

users_db = {
    "lvicente": {"username": "lvicente",
                    "full_name": "Luis Vicente",
                    "email": "lvicente@hangarxxi.com",
                    "disable": False,
                    "password": "123456"
    },
    "lvicente2": {"username": "lvicente2",
                    "full_name": "Luis Vicente 2",
                    "email": "lvicente2@hangarxxi.com",
                    "disable": True,
                    "password": "654321"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

# --------- CRITERIOS DE DEPENDENCIA  ----------------------------
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales de autenticación inválidas",
                            headers={"WWW-Authenticate": "Bearer"})
    if user.disable:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Usuario inactivo")

    return user

# ------------------- SERVICIOS ------------------------------------
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no es corecto")
    
    user = search_user_db(form.username)
    if form.password != user.password:
        raise HTTPException(status_code=400, detail="La contraseña no es corecta")

    return {"acces_token": user.username, "token_type": "bearer"}



@router.get("/me")
async def me(user: User = Depends(current_user)):
    return user