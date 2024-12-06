import json
from collections import Counter

with open("clinica.json", mode="r") as json_file:
    data = json.load(json_file)

# definir las operaciones
# reporte de cantidad de pacientes por enfermedad

def reporte_cantidad(datos, key):
    """

    :param datos:
    :return: un resumen en forma de diccionario
    """
    lista = []
    for identificacion in datos:
        lista.extend(datos[identificacion][key])
    return Counter(lista)

def comparacion_pacientes(datos, id1, id2):
    paciente1 = datos[id1]
    paciente2 = datos[id2]

    enfermedades_comunes = set(paciente1["enfermedad"]).intersection(paciente2["enfermedad"])
    medicamentos_comunes = set(paciente1["medicamento"]).intersection(paciente2["medicamento"])

    return enfermedades_comunes, medicamentos_comunes

condicion = True
while condicion:
    # inputs: tipo de consulta
    condicion = False