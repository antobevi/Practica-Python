### Lambdas ###
# Son como funciones con la particularidad de que son anonimas, es decir, que no tienen nombre

# Puedo almacenarla en variables
sum_to_values = lambda first_value, second_value: first_value + second_value
print (sum_to_values(21, 21))

def sum_three_values_to(third_value):
    return lambda first_value, second_value: first_value + second_value + third_value

print(sum_three_values_to(5)(10, 20))
# Los parametros de la funcion lambda estan implicitos en los parametros de la funcion principal