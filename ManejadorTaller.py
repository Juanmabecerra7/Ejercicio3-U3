from Inscripcion import Inscripcion
from TallerInscripcion import Taller
import numpy as np
import csv

class ManejadorTaller:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    __inscripciones: list

    def __init__(self, dimension, incremento=5):
        self.__taller = np.empty(dimension, dtype = Taller)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__inscripciones = []

    def agregarTaller(self, unTaller):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__taller.resize(self.__dimension, refcheck=False)
        self.__taller[self.__cantidad] = unTaller
        self.__cantidad += 1

    def test(self):
        archivo = open("Talleres.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
             idTaller = fila[0]
             nombre= fila[1]
             vacantes = fila[2]
             monto  = fila[3]
             unTaller = Taller(idTaller, nombre, vacantes, monto)
             self.agregarTaller(unTaller)
        archivo.close()
        
    def __str__(self):
        s = " "
        indice = 0
        while indice < self.__dimension:
            s += str(self.__taller[indice]) + "\n"
            indice += 1
        return s

    def buscarTaller(self, nombre):
        indice = 0
        while indice < self.__dimension:
            if nombre in Taller.getNombre(self.__taller[indice]):
                Taller.modificarCupo(self.__taller[indice])
                return self.__taller[indice]
            indice += 1
    

    def InscribirPersona(self, persona, MI):
        pago = None
        fecha = input("Ingrese la fecha de la inscripcion: ")
        nombre = input("Ingrese el nombre del taller: ")
        unTaller = self.buscarTaller(nombre)
        inscripcion = Inscripcion(fecha, pago,persona,unTaller)
        MI.test(inscripcion)
        self.__inscripciones.append(inscripcion)

    def mostrarInscripciones(self):
        for inscripciones in self.__inscripciones:
            print(inscripciones)