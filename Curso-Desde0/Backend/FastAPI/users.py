import fastapi
from fastapi import HTTPException
from pydantic import BaseModel

# Creacion de una API simple para usuarios generales

app = fastapi.FastAPI()

# Para iniciar el servidor: uvicorn users:app --reload

# Para crear una API de usuarios, primero necesitamos primero una entidad para definir usuarios
"""
class User:
    name: str
    surname: str
    age: int
    web_page_url: str

    def __init__(self, name: str, surname: str, age: int, web_page_url: str) -> None:
        self.__name = name # Propiedad privada
        self.__surname = surname
        self.__age = age
        self.web_page_url = web_page_url # Propiedad publica

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def get_web_page_url(self):
        return self.web_page_url
"""
# BaseModel nos brinca la capacidad de crear una entidad y la tratemos de diferentes formas, entonces, podemos crear la
# entidad sin hacer lo de antes y agregar el constructor y demas..
class User(BaseModel): # User hereda un comportamiento de BaseModel
    id: int
    name: str
    surname: str
    age: int
    web_page_url: str

# Todavia no tenemos una bd con usuarios, asique creamos una lista de usuarios random
users = [User(id = 1, name = "Antonella", surname = "Bevilacqua", age = 25, web_page_url = "https://www.linkedin.com/in/antonella-bevilacqua-a82631146/"),
         User(id = 2, name = "Morita", surname = "Bevilacqua", age = 9, web_page_url = "No Page Found"),
         User(id = 3, name = "Uma", surname = "Bevilacqua", age = 12, web_page_url = "No Page Found")]

# GET
@app.get("/users")
async def get_users():
    return users

def search_user(id: int):
    try:
        return list(filter(lambda user: user.id == id, users))[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

# Si nos piden un usuario en particular:
# Path
# Por ejemplo: /users/1
@app.get("/users/{id}")
async def get_specific_user(id: int):
    return search_user(id)

# Query
# Por ejemplo: /users/?id=1&name="Antonella"
@app.get("/users/")
async def get_another_specific_user(id: int):
    return search_user(id)

# POST
@app.post("/users/", response_model=User, status_code=201) # response_model sirve para la documentacion, saber que se espera que retorne
async def new_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=409, detail="El usuario ya existe!") # propaga la excepción
        #return HTTPException(status_code=204, detail="El usuario ya existe!")
        #return {"error": "El usuario ya existe!"}
    else:
        users.append(user)
        return user

# PUT
# Actualizaremos un usuario completo, aunque solo queramo actualizar la url de su pagina web, por ejemplo.
@app.put("/users/")
async def update_user(user: User):
    if type(search_user(user.id)) != User:
        return {"error": "El usuario no existe!"}
    else:
        for index, saved_user in enumerate(users):
            if saved_user.id == user.id:
                users[index] = user  # Reemplazamos el objeto completo
        return search_user(user.id)

""" La función enumerate recibe un objeto iterable y retorna tuplas en las que cada una contiene 
un elemento del objeto que recibe y un índice que indica su posición"""

# DELETE
@app.delete("/users/{id}")
async def delete_user(id: int):
    if type(search_user(id)) == User:
        for index, saved_user in enumerate(users):
            if saved_user.id == id:
                users.pop(index)
        return users
    else:
        return {"error": "El usuario no existe!"}