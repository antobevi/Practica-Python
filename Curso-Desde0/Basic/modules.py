### Modulos ###
# Es un concepto similar a las librerias, ya que los modulos me permiten acceder a código de otros archivos
# Esto nos ayuda a evitar repetir codigo
# Ejemplo, quiero importar funciones que tengo en un archivo determinado:

#import funciones
from functions import sum_two_values # Para importar solo una funcion
from math import pi as PI_VALUE

#funciones.sum_two_values(21, 21) # Si importo el archivo completo
sum_two_values(21, 21) # Si importo la funcion en particular

print(PI_VALUE)