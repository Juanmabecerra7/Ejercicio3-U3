from Inscripcion import Inscripcion
import numpy as np

class ManejadorInscripcion:
    __dimension = 0
    __cantidad = 0
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__inscripciones = np.empty(dimension, dtype=Inscripcion)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarInscripcion(self, unaInscripcion):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__inscripciones.resize(self.__dimension, refcheck=False)
        self.__inscripciones[self.__cantidad] = unaInscripcion
        self.__cantidad += 1

    def test(self, unaInscripcion):
        self.agregarInscripcion(unaInscripcion)


    def __str__(self):
        indice = 0
        s = ""
        while indice < self.__cantidad:
            s += str(self.__inscripciones[indice]) + "\n"
            indice += 1
        return s
    
    def buscarPersona(self, dni):
        indice = 0
        bandera = False
        while bandera == False and indice < self.__cantidad:
            if Inscripcion.getDniPersona(self.__inscripciones[indice]) == int(dni):
                nombrePersona = Inscripcion.getNombrePersona(self.__inscripciones[indice])
                monto = Inscripcion.getMontoTaller(self.__inscripciones[indice])
                nombreTaller = Inscripcion.getNombreTaller(self.__inscripciones[indice])
                print(f"{nombrePersona} esta inscrita en el taller {nombreTaller} y adeuda {monto}")
                bandera = True
            indice += 1

    def listarInscriptosTaller(self, ID):
        indice = 0
        s = ""
        while indice< self.__cantidad:
            if int(Inscripcion.getIDTaller(self.__inscripciones[indice])) == int(ID):
                s += str(self.__inscripciones[indice]) +"\n"
            indice += 1
        return s
    
    def registrarPago(self, dni):
        indice = 0
        bandera = False
        while bandera == False and indice < self.__cantidad:
            if int(Inscripcion.getDniPersona(self.__inscripciones[indice])) == int(dni):
                Inscripcion.modificarPago(self.__inscripciones[indice])
                print("El pago se modifico con exito")
                bandera = True
            indice += 1