### Expresiones regulares ###
# Nos sirven para comprobar si una cadena de texto contiene determinados elementos y obtener las coincidencias
import re

un_string = "Aprendiendo sobre expresiones regulares en Python! Nivel Intermedio"
otro_string = "No estoy aprendiendo sobre expresiones regulares en Python"

# Match
# Dado un patron y un string, retorna lo que coincida con dicho patron y si no, retorna none
print(re.match("Aprendiendo", un_string)) # Nos sale que entre los caracteres 0 y 11 encuentra una coincidencia
print(re.match("aprendiendo", otro_string)) # Nos retorna None
print(re.match("expresiones regulares", un_string)) # Nos retorna None ya que al no estar al ppio de la cadena no lo encuentra, siempre busca al principio!

match_var = re.match("Aprendiendo", un_string, re.I) # El 3er parametro es un flag. I, por ejemplo, ignora mayus
print(match_var)
print(match_var.span()) # SPAN nos retorna el rango en que encuentra la coincidencia
start, end = match_var.span()
print(f"Rango inicial: {start}, Rango final: {end}")
print(un_string[start:end])

otro_match_var = re.match("expresiones regulares", otro_string, re.I) # El 3er parametro es un flag. I, por ejemplo, ignora mayus
if otro_match_var is not None: #otro_match_var != None es otra opcion
    print(otro_match_var)
    print(otro_match_var.span())  # SPAN nos retorna el rango en que encuentra la coincidencia
    otro_start, otro_end = otro_match_var.span()
    print(f"Rango inicial: {otro_start}, Rango final: {otro_end}")
    print(otro_string[start:end])

# Search
# A diferencia de match, el search puede encontrar el patrón a lo largo de todo el string, no solo al principio
# Devuelve solo la primera ocurrencia aunque este mas de una vez
search_var = re.search("Python", un_string, re.I)
print(search_var)
un_start, un_end = search_var.span()
print(f"Rango inicial: {un_start}, Rango final: {un_end}")
print(un_string[un_start:un_end])

# Find all
# No retorna un solo objeto, si no un listado con las veces que encontro dicho objeto
findall_var = re.findall("Python", un_string, re.I)
print(findall_var)

# Split
# Separa en strings cada vez que encuentra el patrón que le pasemos y los guarda en una lista
split_var = re.split("!", un_string)
print(split_var)

# Sub
# Reemplaza el string que le indiquemos por el otro que le indiquemos en el 2do parametro
sub_var = re.sub("Python", "Java", un_string, re.I)
print(sub_var)
print(re.sub("[e|E]xpresiones [r|R]egulares", "RegEx", un_string))

## Patrones
# Los patrones son cadenas de texto que hacen referencia a una expresion regular

pattern = r"[eE]xpresiones [rR]egulares" # La r es porque hace referencia a una expresion regular
example_one = re.search(pattern, un_string)
print(example_one)
start, end = example_one.span()
print(un_string[start:end])

pattern = r"[eE]xpresiones [rR]egulares|Python"
print(re.findall(pattern, un_string))

pattern = r"[a-z]" # Solo letras de la a a la z en minuscula
print(re.findall(pattern, un_string))

pattern = r"\d" # Busca solo numeros
print(re.findall(pattern, un_string))

pattern = r"\D" # Busca solo letras
print(re.findall(pattern, un_string))

pattern = r"[eE]." # Busca las coincidencias con la letra e y las devuelve con el caracter que esta a continuacion
print(re.findall(pattern, un_string))

pattern = r"[eE].*"
print(re.findall(pattern, un_string))