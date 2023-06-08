from Persona import Persona
from TallerInscripcion import Taller

class Inscripcion:
    __fecha: str
    __pago: int
    __persona: object
    __taller: object

    def __init__(self, fecha, pago, persona, taller):
        self.__fecha = fecha
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller

    def getDniPersona(self):
        return Persona.getDni(self.__persona)
    
    def getNombrePersona(self):
        return Persona.getNombre(self.__persona)
    
    def getNombreTaller(self):
        return Taller.getNombre(self.__taller)
    
    def getMontoTaller(self):
        return Taller.getMonto(self.__taller)
    
    def getIDTaller(self):
        return Taller.getID(self.__taller)
    
    def __str__(self):
        nombre = Persona.getNombre(self.__persona)
        nombre_taller = Taller.getNombre(self.__taller)
        cadena = f"FECHA: {self.__fecha}"+" "+f"PAGO: {self.__pago}" + "\n"
        cadena += f"PERSONA: {nombre}"+"    "+f"TALLER: {nombre_taller}"
        return cadena
    
    def modificarPago(self):
        self.__pago = True