#11-6-2024 0.42
#pip install "fastapi[all]"
from fastapi import FastAPI

#pip install "uvicorn[standard]"
#WARNING: The script uvicorn.exe is installed in 'C:\Users\Luis Vicente\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
#from typing import Union

app = FastAPI()

#para ejecutar esto: uvicorn main:app --reload  --> que abre un servidor, normalmente en: http://127.0.0.1:8000
#******************************************************************************************************************
# Routers
from routers import products, users, users_basic_auth, users_jwt_auth, users_db
app.include_router(products.router)
app.include_router(users.router)
app.include_router(users_basic_auth.router)
app.include_router(users_jwt_auth.router)
app.include_router(users_db.router)


#******************************************************************************************************************
# Ficheros estáticos
from fastapi.staticfiles import StaticFiles
app.mount("/estatico", StaticFiles(directory="estatico"), name="static")
#******************************************************************************************************************


#******************************************************************************************************************
@app.get("/")
async def root():
    return "Hola FastAPI"


#******************************************************************************************************************
@app.get("/url")
async def url():
    return { "url": "https://mouredev.com/python" }

print("Documentación con Swagger: http://127.0.0.1:8000/docs")
print("Documentación con Redoclyr: http://127.0.0.1:8000/redoc")