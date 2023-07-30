### Tipos de errores ###
# Errores que Python ya tiene capturados

# SyntaxError
# Ejemplo: print "Hello World" (faltan los parentesis)
print("Hello World")

# NameError
# Ejemplo:  print(name) (la variable no esta definida)
name = "Morita"
print(name)

# IndexError
programming_languages = ["Python", "Java", "C", "Kotlin", "Ruby", "JavaScript", "C++", "Swift", "Dart", "C#"]
# Ejemplo: print(programming_languages[10]) (el indice indicado esta fuera de rango)
print(programming_languages[0])
print(programming_languages[-1])

# ModuleNotFoundError
# Ejemplo: import maths (no existe un modulo llamado maths, existe uno llamado math)
import math

# AttributeError
# Ejemplo: print(math.PI) (no encuentra el atributo pi de la libreria math porque esta en mayuscula)
print(math.pi)

# KeyError
one_dict = {"Nombre":"Antonella", "Apellido":"Bevilacqua", "Edad":25, "Mascotas":["Morita", "Uma"]}
# Ejemplo: print(one_dict["Perritos"]) (no existe la clave que intentamos consultar)
print(one_dict["Mascotas"])

# TypeError
one_list = [0, 1, 2, 3, 4]
# Ejemplo print(one_list["1"]) (los indices deben ser de tipo integer, no string. Error de tipo de dato)
print(one_list[1])

# ImportError
# Ejemplo: from math import PI (no se puede importar pi de la libreria math, no encuentra PI en mayusculas)
from math import pi # si encuentra pi en minuscula
print(pi)

# Value Error
# Ejemplo: number = int("10 años") (no puede convertir este string en particular a un entero)
number = int("10")
print(type(number))

# ZeroDivisionError
# Ejemplo: print(4/(2-2)) (no se puede realizar una division por cero)
print(4/(4-2))