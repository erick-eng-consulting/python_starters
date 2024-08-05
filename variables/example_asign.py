# var = 100
# print(var)
#
# # var = var + 1
# # var++
# var += 1
# print(var)
# var += 2
# print(var)

# ejercicio
# producto = 1000
# el impuesto es de 13%
# calcular el precio final usando el *= +=
"""

"""
producto = 1000
impuesto = 13
print(f'El precio del producto sin impuesto es {producto}')
print(f'El impuesto es {impuesto}%')

impuesto /= 100  # evita esto: impuesto = impuesto / 100
print(f'El precio del producto {producto * impuesto}')
impuesto += 1    # 1.13

producto *= impuesto
print(f'El precio final es {producto}')

pass