import fastapi

app = fastapi.FastAPI()

# Accedemos al contexto de FastAPI
# El / es la raiz de donde se esta desplegando nuestra api, por ejemplo, http://127.0.0.1:8000/ es la raiz
# Desde el navegador solo podemos hacer la operacion gET, si queremos hacer otras, vamos a necesitar una herramienta
# como por ejemplo, Postman (cliente para ejecutar peticiones a un API)
@app.get("/") # GET (obtener) es una de las operaciones disponibles dentro de la comunicacion HTTP
async def get_string():
    # Funcion asincrona
    return "Siempre que llamamos a un servidor, las operaciones que se ejecutan deben ser Asincronas"

# Petición Sincrona
# Si llamamos al servidor, la aplicacion no puede hacer nada hasta que el servidor nos responda.
# Espera a la respuesta del servidor para continuar.

# FastAPI nos ofrece un servidor local para poder probar lo que estamos haciendo llamado Uvicorn.
# Iniciar el servidor uvicorn: uvicorn main:app --reload
# URL local: http://127.0.0.1:8000

@app.get("/google-url")
async def get_google_URL():
    return {"google-url": "https://www.google.com.ar"}

# Otras operaciones dentro de la comunicacion HTTP (solo las mas comunes, pero hay mas):
# POST (crea un nuevo recurso)
# PUT (actualiza un bloque completo. Por ejemplo, pasamos el usuario completo para que lo actualice)
# PATCH (actualiza una parte de un bloque, no completo. Por ejemplo, del usuario solo pasamos el nuevo email)
# DELETE

### Routers ###
# Enrutamiento
# Desde el main necesitamos la referencia a las rutas de users y productos. Tanto main, como users y products
# conforman una API general que estamos creando, pero para manejarlo todo desde un lugar necesitamos crear un Router
# Esto nos va a permitir lanzar un unico servidor y aun asi acceder a todas las "apis" que tengamos como users y products.
# Entonces, importamos el Router que creamos:

from Routers import products
from Routers import users

# Routers
app.include_router(products.router) # Router de productos
app.include_router(users.router) # Router de users