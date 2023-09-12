# API de Productos

from fastapi import APIRouter

# users y products van a trabajar dentro de la API general. Sin embargo, no van a ser una API
# como entidad en si, si no que van a ser un Router, que es lo que necesitamos crear a continuación
# Luego, este Router lo importamos en el main
router = APIRouter(prefix="/products", 
                   tags=["products"], # Los Tags sirven para la documentación, agrupa e indica con una etiqueta para lo relacionado con este archivo
                   responses={404: {"Message":"No se ha encontrado"}}) # En caso de no encontrarlo, tira este msj de error
# Si yo indico un prefijo, no hace falta repetirlo en las operaciones. Por ejemplo, no hace falta indicar
# el "/products" en @router.get("/products")

products = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"]

@router.get("/")
async def get_products():
    return products

# Si nos piden un producto en particular:
# Path
# Por ejemplo: /products/1
@router.get("/{id}")
async def get_specific_product(id: int):
    return products[id]