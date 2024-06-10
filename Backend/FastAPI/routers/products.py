from fastapi import APIRouter

router = APIRouter(prefix="/products", # ya no hace falta indicar en los gets, puts... el "/products"
                   tags=["products"],  # es para que en la documentación separe los servicios de esta API
                   responses= {404: {"message": "No encontrado"}}
                  )
#******************************************************************************************************************
products_list = ["Producto1","Producto2","Producto3","Producto4","Producto5"]


@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]