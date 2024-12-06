# se reciben 3 parametros para ser utilizados por una funcion
# y se van realizar varios calculos
# a + b / c
# a + b + c
# a * b + c

# la definicion de la funcion
def funcion1(a, b, c):
    # el scope define el espacio donde las variables se definen/ viven/ se pueden utlizarse
    resultado1 =  a + b / c
    resultado2 = a + b + c
    resultado3 = a * b + c

    return [resultado1, resultado2, resultado3]  # empaquetando varios valores

# la invocacion o el llamado
var1 = 1
var2 = 4
var3 = 6

res1, res2, res3 = funcion1(int("10"), var2, var3)
print(res1, res2, res3)

# como hacer para retornar varios valores