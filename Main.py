from ManejadorTaller import ManejadorTaller
from ManejadorPersona import ManejadorPersona
from ManejadorInscripcion import ManejadorInscripcion

if __name__=="__main__":
    MT = ManejadorTaller(3)
    MP = ManejadorPersona()
    MI = ManejadorInscripcion(1)
    MT.test()
    print(str(MT))
    while 1 != 0:
        print("1: Inscribir a una persona")
        print("2: Consultar una Inscripcion")
        print("3: Consultar Inscriptos")
        print("4: Registrar Pagos")
        print("5: Salir")
        opcion = int(input("Ingrese la opcion deseada: "))
        if opcion == 1:
            MP.cargarPersona(MT, MI)
            print("La persona de inscribio con exito")
        elif opcion == 2:
            dni = input("Ingrese el dni de la persona a consultar: ")
            MI.buscarPersona(dni)
        elif opcion == 3:
            ID = input("Ingrese la ID de un Taller: ")
            print(str(MI.listarInscriptosTaller(ID)))
        elif opcion == 4:
            dni = input("Ingrese el dni de la persona a registrar el pago: ")
            MI.registrarPago(dni)
        elif opcion == 5:
            exit()
        else:
            print("----Opcion Incorrecta")