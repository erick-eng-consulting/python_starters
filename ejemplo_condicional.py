# esto es un verificador de edad como criterio de permiso de conducir

# edad = 10
#
# # el if puede vivir solito sin la compañia del else
# if edad >= 18:
#     print("puedo manejar")
# #el else no puede vivir sin el if
# else:
#     print("soy menor de edad")

edad = 10

# se puede manejar desde los 18 hasta los 99
# otras edades no se puede manejar

# preguntar por un rango de edad

# por el limite izquierdo
18 <= edad

#por el limite derecho
edad <= 99

condicion = 18 <= edad & edad <= 99
pass # una palabra reservada. muy conveniente. sirve como placeholder

# if edad >= 18:
#     print("puedo manejar")
# elif edad < 99:
#     print("manejar")
# elif edad > 99:
#     print("soy super abuelo")
# else:
#     print("no puedo manejar")