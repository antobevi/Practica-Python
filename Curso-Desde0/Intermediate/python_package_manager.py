### Gestor de Paquetes Python PIP ###
# Cuando quiero manejar con dependencias, y usar librerias que tal vez no estan dentro de Python
# Para cualquier modulo que no tengamos descargado vamos a tener que usar esto

# PIP
# Sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python.
# Muchos paquetes pueden ser encontrados en el Python Package Index.
# pip install pip

import numpy # Provee array de items homogeneos sobre el cual pueden realizarse operaciones matematicas/algebraicas
import pandas # pip install pandas
import requests

print(numpy.pi)
print(numpy.version.version)

numpy_array = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(numpy_array)
print(numpy_array * 2)

# pip list Nos retorna las librerias que tenemos instaladas
# Para desinstalar: pip unistall pandas
# Para ver la info de la libreria instalada como lugar, version, etc.: pip show numpy

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response) # El 200 indica que salio bien
print(response.status_code)
print(response.json())

#   MyFirstPackage: arithmetics
from MyFirstPackage import arithmetics

print(arithmetics.sum_two_values(11, 10))