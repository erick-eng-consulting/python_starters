# ejemplo para conjuntos
# amigos, frutas preferidas

carlos = {"manzana", "mango", "uva"}

juan = {"pera", "uva", "naranja"}

# si carlos y juan comparten las frutas
# cuales son las frutas que van a tener en los 2?

# la operacion union
canasto = carlos.union(juan)
print(canasto)

# si carlos y juan revisan las frutas.
# cual o cuales son las frutas que tienen en comun?
print(carlos.intersection(juan))

# cuales los frutas que tiene carlos pero no juan?
print(carlos.difference(juan))

print(carlos - juan)


# suponga que un canasto hay muchas frutas
# pera, banano, naranja, pera, limon, banano

# cuales son los tipos de frutas que estan en el canasto?

lista_frutas = ["pera", "banano", "naranja", "pera", "limon", "banano"]
contenido_canasto = set(lista_frutas)
print(contenido_canasto)

