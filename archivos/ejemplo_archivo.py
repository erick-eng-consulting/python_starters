# vamos a suponer que el archivo mi_dato.txt existe

# y lo vamos a leer

with open("mi_dato.txt", mode="r") as mi_archivo:
    var = mi_archivo.read()

print(var)