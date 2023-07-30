### List Comprehension ###
# Forma de crar listas mas facil y rapido ya que las creamos a partir de otras

original_list = list()
original_list = [35, 24, 62, 52, 30, 30, 17]

new_list = [i for i in original_list]
print(new_list)

other_list = [i for i in range(7)]
print(other_list)

other_list_1 = list(range(8))
print(other_list_1)

other_list_2 = [i + 1 for i in range(9)]
print(other_list_2)

def plus_five(number: int):
    return number + 5

other_list_3 = [plus_five(i) for i in range(10)] # rango de 0...9
print(other_list_3)