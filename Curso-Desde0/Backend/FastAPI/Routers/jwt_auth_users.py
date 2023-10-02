from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from jose import JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta # datetime para trabajar con fechas y timedelta para operar con fechas

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login") # end point que se llama login

# Contexto de encriptacion
crypt = CryptContext(schemes="bcrypt") # Los esquemas definen el algoritmo de encriptacion a usar
# Vamos a 

# Constantes
ALGORITHM = "HS256" # Algoritmo de encriptacion mas usado
ACCESS_TOKEN_DURATION = 1 # Minutos
SECRET = "RWEbWjLqm2dGLNkwDvNFZ5dsopiCGbK3OMUGzL0jar1YVSJznX" # Para realizar la encriptacion y decriptacion se utiliza una clave que solo deberíamos conocer nosotros

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
                        "password": "$2a$12$PSG15eLZUzJB9SkVyZa3eObDhFP5RPtUQLiMU1mZwLnTd22M0Pv2G"}, # la contraseña no se puede guardar en bd asi nomas, deberia guardarse con un hash al menos
            "morita": {"name": "Morita",
                       "surname": "Bevilacqua",
                       "age": 9,
                       "email": "",
                       "username": "Morita",
                       "disable": False,
                       "password": "$2a$12$9L6DnFlXSre90/4gMXRIuuyfEyE3OBNf9goadzle4ZGjNXHaKUrDC"},
            "momo": {"name": "Uma",
                    "surname": "Bevilacqua",
                    "age": 13,
                    "email": "",
                    "username": "Momo",
                    "disable": False,
                    "password": "$2a$12$SyooUbjEeMGMJ3XwrDGvQuIqmOzNRuC7RM/bYVEjuUrFpJ.WgYx9K"}}

def search_user_db(username: str = Depends(oauth2)):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str ): # De esta forma al retornarlo no mostramos la contraseña
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)): # usuario autenticado que obtenemos a partir del token

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales de autenticación inválidas", 
                            headers={"WWW-Authenticate": "Bearer"})  # headers: tambien sigue un estandar, nos da mas informacion   
    
    try:
        # Retorna un diccionario con varios datos del usuario
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception
    
    return search_user(username)

async def current_user(user:User = Depends(auth_user)):
    # El token ya no es el username que esta en el user db
    # A partir del token, se busca el usuario (si aun no expiro y si existe), si esta ok chequeamos si no esta deshabilitado
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")

    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario y/o la contraseña son incorrectos.")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="El usuario y/o la contraseña son incorrectos.")
    
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION) # hora en que se genero el token + el tiempo que queremos que dure = 1 min
    expire = datetime.utcnow() + access_token_expiration # hora actual de login + tiempo de expiracion = hora de expiracion

    access_token = {"sub":user.username, "exp": expire}

    # El concepto de autenticacion y de access token tiene asociado una duracion del token
    # Cuando uno se auntica, esa autenticacion dura solo un tiempo determinado
    # Encriptamos el access token
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def get_user_profile(user: User = Depends(current_user)):
    return user