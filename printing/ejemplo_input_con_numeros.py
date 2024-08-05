# Esto es un ejemplo de input con numeros

edad = input('Favor ingresa tu edad:')

try:
    edad = int(edad) + 10
except:
    pass

print('Tu edad es', edad)