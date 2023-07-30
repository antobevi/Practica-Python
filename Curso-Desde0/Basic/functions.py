### Funciones ###
import string

# Definimos una funcion que no retorna nada
def my_function():
    print("Esta es mi primera funcion en Python")

# Definimos una funcion que retorna un valor
def sum_two_values(first_number: int, second_number: int):
    print(first_number + second_number)

def print_name(name: string, surname: string):
    print(f"El nombre completo es: {name} {surname}")

# Llamamos a las funciones definidas anteriormente
my_function()
sum_two_values(4, 10)
print_name("Antonella", "Bevilacqua")
