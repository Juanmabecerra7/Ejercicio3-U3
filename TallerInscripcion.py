class Taller:
    __idTaller: int
    __nombre: str
    __vacantes: int
    __monto:int

    def __init__(self, idTaller, nombre, vacantes, monto):
        self.__idTaller =idTaller
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__monto = monto

    def getNombre(self):
        return self.__nombre
    
    def getMonto(self):
        return self.__monto
    
    def getID(self):
        return self.__idTaller
    
    def modificarCupo(self):
        self.__vacantes = int(self.__vacantes)-1

    def __str__(self):
        return str(self.__idTaller)+" "+str(self.__nombre)+" "+str(self.__vacantes)+" "+str(self.__monto)
    
    