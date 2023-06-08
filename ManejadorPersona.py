from Persona import Persona

class ManejadorPersona:
    def __init__(self):
        self.__lista = []
        self.__cantidad = 0

    def agregarPersona(self,unaPersona):
        self.__lista.append(unaPersona)

    def cargarPersona(self, MT, MI):
        nombre = input("Ingrese el nombre de la persona: ")
        direccion = input("Ingrese la direccion de las persona: ")
        dni = int(input("Ingrese el DNI de la persona: "))
        unaPersona = Persona(nombre, direccion, dni)
        self.__cantidad += 1
        self.agregarPersona(unaPersona)
        MT.InscribirPersona(unaPersona, MI)


    def __str__(self):
        indice = 0
        s = ""
        while indice < self.__cantidad:
            s += str(self.__lista[indice]) + "\n"
            indice += 1
        return s