
# lista de colores

colores = ["blanco", "azul", "rojo", "azul", "amarillo", "rojo"]
print(colores)

from collections import Counter

resumen = Counter(colores)

# como iterar un diccionario
for color in resumen.keys():
    print(f"El color {color} esta esta escrito {resumen[color]}")
pass