### Manejo de archivos ###

txt_file = open("file.txt", "r+")
# r+ lectura y escritura pero sin sobreescribir
# w+ lectura y escritura y sobreescribe lo existente

#print(txt_file.read())
#print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
##print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)

txt_file.write("\nY tambien me gustaría tener una cafeteria algun dia.")
print(txt_file.readline())