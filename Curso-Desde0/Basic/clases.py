# Clases
import string


class Person:
    # Para las clases los nombres van en CamelCase
    # Para las variables, nombres de funciones y demas los nombres van en snake_case
    """Instruccion del sistema que se utiliza cuando se quiere crear una clase, método, función, bucle o
    condicional, pero en el que todavía no se quiere definir ningún comportamiento. Evita que el programa
    emita un msj de error"""
    pass

    # Constructor de la clase que no retorna nada (el None se puede omitir)
    def __init__(self, name: string, surname: string, age: int, alias="Sin Alias") -> None:
        self.__name = name # con los guiones bajos dobles hacemos que una variable sea privada
        self.__surname = surname # con los guiones bajos dobles hacemos que una variable sea privada
        self.__age = age # con los guiones bajos dobles hacemos que una variable sea privada
        self.full_name = f"{name} {surname}" # sin guiones bajos dobles la variable es publica
        self.alias = alias # sin guiones bajos dobles la variable es publica

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def walk(self):
        print(f"{self.full_name} esta caminando...")


# Las clases pueden llamarse con o sin parentesis
# print(Person)
# print(Person())

una_persona = Person("Antonella", "Bevilacqua", 25)

print(f"{una_persona.get_name()} {una_persona.get_surname()} con alias {una_persona.alias}")
una_persona.walk()
print(una_persona.get_name())
