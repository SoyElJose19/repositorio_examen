import time,os
from FUNCIONES import *
while True:
    os.system("cls")
    print("\tDATOS TRABAJADORES")
    print("1.- Asignar Sueldos Aleatorios")
    print("2.- Clasificar sueldos")
    print("3.- Ver Estadísticas")
    print("4.- Reporte De Sueldos")
    print("5.- Salir")
    opc = int(input("Ingrese Opción: "))
    os.system("cls")
    if opc ==1:
        asignar_sueldo()
    elif opc ==2:
        clasificar_sueldos()
    elif opc ==3:
        ver_estadisticas()
    elif opc ==4:
        reporte_sueldos()
    elif opc ==5:
        salir()
    else:
        print("OPCIÓN INCORRECTA...INGRESE OPCIÓN ENTRE 1 Y 5")
    time.sleep(3)
    
    