### Manejo de errores con excepciones ###

number_one = 21
number_two = '21'

# try except
try:
    print(number_one + number_two)
    print("No se ha producido ningun error..") # Si la linea anterior falla, lo que este a continuacion no se
                                               # va a ejecutar, va a ir a lo que definimos en el except
except:
    print("Se ha producido un error!")

# try except else
try:
    print(number_one + 21)
    print("No se ha producido ningun error..")
except:
    print("Se ha producido un error!")
else:
    print("La ejecución continua correctamente")
    # Esto se ejecuta cuando no se produce la excepcion, es decir, si no ocurre ningun error en el bloque del try

# finally
try:
    print(number_one + '23')
    print("No se ha producido ningun error..")
except:
    print("Se ha producido un error!")
else:
    print("La ejecución continua correctamente")
finally:
    print("La ejecución continua..")
    # El finally se ejecuta siempre pase lo que pase

# Excepciones por tipo para capturar errores muy concretos
try:
    print(number_one + number_two)
    print("No se ha producido ningun error..")
except TypeError: # Esta excepcion SOLO se ejecuta si ocurre un error de tipo TypeError
    print("Se ha producido un error de tipo TypeError!")

try:
    print(number_one + 21)
    print("No se ha producido ningun error..")
except ValueError: # SOLO captura errores de tipo ValueError, tipo de error definido por el sistema
    print("Se ha producido un error de tipo ValueError!")

try:
    print(number_one + number_two)
    print("No se ha producido ningun error..")
except TypeError: # Esta excepcion SOLO se ejecuta si ocurre un error de tipo
    print("Se ha producido un error de tipo TypeError!")
except ValueError:  # Solo captura errores de tipo ValueError, tipo de error definido por el sistema
    print("Se ha producido un error de tipo ValueError!")

# Capturar la información de la excepcion
try:
    print(number_one + number_two)
    print("No se ha producido ningun error..")
except TypeError as error:
    print("Se ha producido un error de tipo TypeError!")
    print(error)

try:
    print(number_one + number_two)
    print("No se ha producido ningun error..")
except ValueError as valueError:  # Si ocurre un error de tipo ValueError lo captura
    print("Se ha producido un error de tipo ValueError!")
    print(valueError)
except Exception as exceptionError: # Si no, lo captura aca de forma mas general
    print("Se ha producido un error!")
    print(exceptionError)
    # except Exception es lo mismo que poner el except solo como al principio