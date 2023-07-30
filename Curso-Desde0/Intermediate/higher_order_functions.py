### Funciones de orden superior ###
# Es la capacidad de poder manipular y utilizar funciones como cualquier otro dato, por ejemplo,
# las funciones pueden tomar otras funciones como argumentos y/o devolver funciones como resultado

from functools import reduce

def sum_one_to(value):
    return value + 1

def sum_two_values_and_add_one(first_value, second_value, f_sum_one):
    return f_sum_one(first_value + second_value)

print(sum_two_values_and_add_one(21, 40, sum_one_to))

### Closures ###
''' Un closure es una función junto con su entorno léxico capturado. El entorno léxico se refiere al ámbito de 
variables en el que se definió la función cuando fue creada. Cuando una función se define en otro contexto, 
pero aún tiene acceso a las variables y parámetros de ese contexto incluso después de que ese contexto 
haya terminado su ejecución, se crea un closure '''

def sum_ten():
    def add_ten(value):
        return value + 10
    return add_ten

add_closure = sum_ten() # sum_ten retorna una funcion
print(add_closure)
print(add_closure(5))

def sum_ten_to(original_value):
    def add_ten_to(value):
        return value + 10 + original_value # se guarda como contexto el original_value, su referencia
    return add_ten_to

add_other_closure = sum_ten_to(5) # sum_ten retorna una funcion
print(add_other_closure)
print(add_other_closure(5))

print(sum_ten_to(5)(6)) # Como si fuera una lambda
# Al resultado de una operacion: sum_ten_to(5) le pasamos el siguiente parametro: 6
# Es decir, es como si tuvieramos lo siguiente: (sum_ten_to(5))(6)
print((sum_ten_to(5))(6))

### Mas sobre Funciones de Orden Superior ###
# Funciones que ya existen en el sistema que podemos utilizar que son de orden superior

# Map
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def multiply_two(value):
    return value * 2
# MAP recibe una funcion y un iterable, a cada elemento de ese iterable se le aplica la funcion
# No modifica la lista original, si no que nos retorna esa lista trasformada
print(list(map(multiply_two, numbers))) # MAP retorna un objeto, asi que lo guardamos en una lista para ver mejor
print(numbers)

print(list(map(lambda number: number * 4, numbers)))
print(numbers)

# Filter
def values_greater_than_five(value):
    return value >= 5

print(list(filter(values_greater_than_five, numbers))) # FILTER retorna un objeto
print(numbers)
print(list(filter(lambda number: number >= 5, numbers)))
print(numbers)

# Reduce: opera entre los valores que va recorriendo

def sum_two_values(first_value, second_value):
    print("First value: ", first_value)
    print("Second value: ", second_value)
    return first_value + second_value

print("- Final result: ", reduce(sum_two_values, numbers)) # 0+1 = 1, 1+2 = 3, 3+3 = 6, 4+6 = 10, ...
print(numbers)