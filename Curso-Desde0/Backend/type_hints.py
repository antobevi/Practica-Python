### Type Hints ###
# Los Type Hints son una nueva sintaxis de Python 3.6+ que nos permite declarar el tipo de una variable.
# Al tipar una variable y especificar el tipo de dato se puede trabajar mejor, ayuda no solo al editor
# si no que tambien ayuda a FastAPI (para validar datos).
# Sin embargo, aunque tipemos una variable, al ser un tipado debil aunque indiquemos un tipo de dato en particular,
# si le asignamos otro tipo Python va a priorizar el tipo de dato asignado. Por ejemplo:

typed_var: int = "Esto es un String"
print(typed_var)
print(type(typed_var))

typed_var = 0.5
print(typed_var)
print(type(typed_var))

typed_var = 5
print(typed_var)
print(type(typed_var))
