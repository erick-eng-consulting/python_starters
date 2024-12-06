# vamos a crear
# una clase para
# caracterizar personas humanos

class Persona:
    # altura, peso, nombre, identificacion

    def __init__(self, nombre):
        # este es el metodo "constructor"
        self.edad = 0
        self.nombre = nombre
        self.cantidad_pasos = 0

    def camine(self, cantidad_pasos):
        # acumular los pasos
        self.cantidad_pasos += cantidad_pasos



juanito = Persona(nombre="Juan")
maria = Persona(nombre="Maria")
pass