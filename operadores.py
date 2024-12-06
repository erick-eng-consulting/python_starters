
precio_naranja = 500

precio_manzana = 400

# pregunta: la naranja vale menos que 1000 colones

resultado = precio_naranja < 1000
print(resultado)

# operaciones con argumento
# las frutas tienen un impuesto
impuesto = 4

#precio_naranja = precio_naranja + precio_naranja * impuesto/100
#precio_naranja = precio_naranja * (1 + impuesto/100)

precio_naranja *= 1 + impuesto / 100

print(precio_naranja)




