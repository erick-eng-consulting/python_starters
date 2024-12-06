

precios = [100, 400, 500, 250]

# utilizar un ciclo

# se puede utilizar la funcion map
# como le aplicamos un descuento del 10 % a los precios?
resultado = list(map(  lambda x: x * 0.9  , precios))

for valor in map(lambda x: x * 0.9 , precios):
    print(valor)
#print(resultado)