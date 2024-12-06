# pedir el nombre

# dar la bienvenida juanito

# con el input puede pedir información desde el usuario

nombre = input("favor escribe tu nombre: ")

# una forma de unir el mensaje de bienvenida junto el nombre

# forma 1
texto = f"bienvenido {nombre}"

print(texto)
print(f"bienvenido {nombre}")

# # forma 2
#
# texto = "bienvenido" + " " + nombre
#
# # forma 3
#
# print("bienvenido", nombre)
#
# # forma 4
# print("bienvenido", end="")
# print(nombre)