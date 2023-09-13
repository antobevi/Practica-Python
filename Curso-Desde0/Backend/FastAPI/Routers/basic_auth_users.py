# Autorizacion OAuth2 (OAuth es un estandar)
# Autorizacion y Autenticacion basica para la API de users
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# OAuth2PasswordBearer es la clase que se encarga de gestionar la autenticacion (con el usuario y la contraseña)
# OAuth2PasswordRequestForm es la forma en que se envia a nuestro backend (API) los criterios de autenticacion
# y de esta forma al capturar el usuario y contraseña podra confirmar si el usuario pertenece al sistema

app = FastAPI()

# Creamos una instancia del sistema de autenticacion
oauth2 = OAuth2PasswordBearer(tokenUrl="login") # url que se encarga de gestionar la autenticacion

class User(BaseModel): # User hereda un comportamiento de BaseModel
    name: str
    surname: str
    age: int
    email: str
    username: str # como vamos a devolver el usuario, no queremos que ese tenga la contraseña y mostrarla
    disabled: bool

# Entidad que representa al usuario que guardamos en base de datos
class UserDB(User): # UserDB hereda de User
    password: str

users_db = {"antobevi": {"name": "Antonella", 
                        "surname": "Bevilacqua", 
                        "age": 25, 
                        "email": "antobevi@gmail.com", 
                        "username": "antobevi", 
                        "disabled": True,
                        "password": "012345"}, # la contraseña no se puede guardar en bd asi nomas, deberia guardarse con un hash al menos
            "morita": {"name": "Morita",
                       "surname": "Bevilacqua",
                       "age": 9,
                       "email": "",
                       "username": "Morita",
                       "disable": False,
                       "password": "678910"},
            "momo": {"name": "Uma",
                    "surname": "Bevilacqua",
                    "age": 13,
                    "email": "",
                    "username": "Momo",
                    "disable": False,
                    "password": "111213"}}

# Funcion para buscar un usuario en la base de datos
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username]) # porque users_db es un diccionario clave usuario valor atributos usuario
        # NOTA: Los ** sirven, en este caso, pasar como argumento un diccionario usando como claves los nombres de los parámetros
        # Mas info: https://j2logo.com/args-y-kwargs-en-python/

def search_user(username: str): # De esta forma al retornarlo no mostramos la contraseña
    if username in users_db:
        return User(**users_db[username])
    
# Criterio de dependencia
# Validamos que el access_token es correcto y lo obtenemos mediante oauth2 que gestiona los tokens
async def current_user(token: str = Depends(oauth2)):
    # Si oauth2 no lo valida el token, FastAPI se encargara de lo que pasa despues
    # Si oauth2 valida el token, necesitamos obtener el usuario
    user = search_user(token) # En este caso el token es el username que esta en el user db
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Credenciales de autenticación inválidas", 
                            headers={"WWW-Authenticate": "Bearer"})
        # headers: tambien sigue un estandar, nos da mas informacion
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")

    return user
    
# Implementamos la operacion de autenticacion
@app.post("/login") # POST nos permite obtener datos enviando datos
async def login(form: OAuth2PasswordRequestForm = Depends()): # Este parametro es para capturar mediante un formulario los datos que nos envian
    # El form va a venir del Depends que es la dependencia de todo el sistema de autenticacion, si el usuario
    # se autentica correctamente, despues viene la parte de que puede hacer en el sistema (autorizacion).
    # La dependencia va a ser el que estemos autenticados o no, para poder acceder a ciertos recursos.
    # En este caso, el Depends() nos indica que vamos a recibir datos pero que no se depende de nada mas.
    user_db = users_db.get(form.username) # Comprobamos si tenemos al usuario
    if not user_db: #not user_db da True si user_db es distinto de None
        raise HTTPException(status_code=400, detail="El usuario y/o la contraseña son incorrectos.")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="El usuario y/o la contraseña son incorrectos.")
    
    # Cuando el usuario se autentica correctamente, el sistema debe devolver un access token ya que asi lo define el estandar
    return {"access_token": user.username, "token_type": "bearer"} # El acces_token debe ser algo encriptado que solo conoce el backend para no estar constantemente autenticando al usuario

@app.get("/users/me") # Le pasamos el token de tipo BEARER, si es correcto nos devolvera el json del usuario 
async def get_user_profile(user: User = Depends(current_user)):
    return user