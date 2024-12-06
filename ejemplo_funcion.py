# vamos a crear un funcion que reste los elementos de una lista

una_lista_de_numeros = [1,2,3,4,5,6,7,8]

def mi_restador(mis_numeros):
    acumulador = 0

    # el ciclo. control de flujo
    for numero in mis_numeros:
        acumulador -= numero

    return acumulador

resultado = mi_restador(una_lista_de_numeros)

print(resultado)