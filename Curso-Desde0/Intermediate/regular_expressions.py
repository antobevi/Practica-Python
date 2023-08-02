### Expresiones regulares ###
# Nos sirven para comprobar si una cadena de texto contiene determinados elementos y obtener las coincidencias
import re

un_string = "Aprendiendo sobre expresiones regulares en Python"
otro_string = "No estoy aprendiendo sobre expresiones regulares en Python"

# Dado un patron y un string, retorna lo que coincida con dicho patron y si no, retorna none
print(re.match("Aprendiendo", un_string)) # Nos sale que entre los caracteres 0 y 11 encuentra una coincidencia
print(re.match("aprendiendo", otro_string)) # Nos retorna None
print(re.match("expresiones regulares", un_string)) # Nos retorna None ya que al no estar al ppio de la cadena no lo encuentra, siempre busca al principio!

match_var = re.match("Aprendiendo", un_string, re.I) # El 3er parametro es un flag. I, por ejemplo, ignora mayus
print(match_var)
print(match_var.span()) # SPAN nos retorna el rango en que encuentra la coincidencia
start, end = match_var.span()
print(f"Rango inicial: {start}, Rango final: {end}")
print(un_string[start])
print(un_string[start:end])

otro_match_var = re.match("expresiones regulares", otro_string, re.I) # El 3er parametro es un flag. I, por ejemplo, ignora mayus
if otro_match_var is not None: #otro_match_var != None es otra opcion
    print(otro_match_var)
    print(otro_match_var.span())  # SPAN nos retorna el rango en que encuentra la coincidencia
    otro_start, otro_end = otro_match_var.span()
    print(f"Rango inicial: {otro_start}, Rango final: {otro_end}")
    print(otro_string[start])
    print(otro_string[start:end])