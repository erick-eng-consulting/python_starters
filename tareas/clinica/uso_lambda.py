
lista_frutas = [
    ("cas", 20),
    ("manzana", 110),
    ("aguacate", 1200),
    ("pina", 800)
]
print(lista_frutas)
# como lo ordenamos por el precio?
lista_frutas.sort(key=lambda x: x[-1], reverse=False)
print(lista_frutas)