### Manejo de archivos ###
import os
import json
import xml
import csv

#               TEXT FILE
txt_file = open("file.txt", "w+")
# r+ lectura y escritura pero sin sobreescribir
# w+ lectura y escritura y sobreescribe lo existente

txt_file.write("Mi nombre es Antonella\nMi apellido es Bevilacqua\nTengo 25 anios\n"+
               "Soy de Buenos Aires, Argentina\nTengo 2 perritas llamadas Uma y Morita\n"+
               "Quiero ser desarrolladora Backend!\n")

txt_file.close()
txt_file = open("file.txt", "r+")

#print(txt_file.read())
#print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
#print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)

txt_file.write("Y tambien me gustaría tener una cafeteria algun dia..\n")

txt_file.close()
txt_file = open("file.txt", "r+")

print(txt_file.readlines())

txt_file.close()

with open("file.txt") as another_txt_file:
    for line in another_txt_file.readlines():
        print(line)

another_txt_file.close()

#os.remove("file.txt") # Eliminamos el archivo

#               JSON FILE

json_file = open("file.json", "r+")

json_test = {
  "name": "Antonella",
  "apellido": "Bevilacqua",
  "age": 25,
  "language": "Spanish"
}

json.dump(json_test, json_file, indent=4) # indent=4 esribe en el file mas "bonito", como se identa json usualmente
# Tener en cuenta que cuanto mas lo identemos mas espacio ocupara
# No se puede usar write porque write espera que le pasemos un string, no un objeto

json_file.close()

with open("file.json") as another_json_file:
    for line in another_json_file.readlines():
        print(line)

another_json_file.close()

json_file_dict = json.load(open("file.json")) # El json pasa a ser un diccionario
print(json_file_dict)
print(type(json_file_dict)) # Por lo que podemos trabajarlo como un diccionario
print(json_file_dict["name"])

#os.remove("file.json") # Eliminamos el archivo

# .xlsx file requiere instalar un modulo para importar la libreria xlrd
# TODO

#               XML FILE
# TODO

#               CSV FILE
''' Es un archivo de texto en el cual los caracteres están separados por comas, haciendo una especie de tabla
en filas y columnas. Las columnas quedan definidas por cada punto y coma (;), mientras que cada fila se define
mediante una línea adicional en el texto'''

csv_file = open("file.csv", "w+")

csv_writer = csv.writer(csv_file) # Crea el writer en base al archivo csv que se le pasa por parameteo
csv_writer.writerow(["name", "apellido", "age", "language"])
csv_writer.writerow(["Antonella", "Bevilacqua", 25, "Spanish"])

csv_file.close()

with open("file.csv") as another_csv_file:
    for line in another_csv_file.readlines():
        print(line)

another_csv_file.close()