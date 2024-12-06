print("El precio de compra")

# input da strings!
precio = input("favor escribir el precio:")

# ocupamos hacer una conversión
precio = float(precio)

#int() # para convertirlo a nuevo entero
#float() # decimal

# asignar el precio con el impuesto del IVA 13%
impuesto = 13
precio_final = precio + precio * impuesto / 100

print(precio_final)