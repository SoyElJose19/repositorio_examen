import random,csv
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]
def asignar_sueldo():
    print("\tASIGNAR SUELDOS")
    while True:
        sueldo=random.randint(300000,2500000)
        for F in trabajadores:
            print("Trabajador:",F,"\nSueldo:",sueldo)
        sueldos.append(sueldo)
        return
def clasificar_sueldos():
    total = 0
    TOTAL_SUELDOS=0
    print("\tCLASIFICAR SUELDOS")
    while True:
        if not sueldos:
            print("NO EXCISTEN SUELDOS PARA LOS TRABAJADORES...INGRESE SUELDOS CON LA OPCIÓN 1")
            return
        else:
            for s in sueldos:
                    for T in trabajadores:
                        print ("Trabajador:",T,"\tSueldo",s)
                    if s <= 800000:
                        print ("Sueldos menores a $800.000 TOTAL",total)
                        total = total +1
                    elif s == 800000 and s >=2000000:
                        print("Sueldos entre $800.000 y $2.000.000 TOTAL:",total)
                        print ("Trabajador:",T,"\tSueldo: ",s)
                        total = total +1
                    elif s >= 2000000:
                        print("Sueldos superiores a $2.000.000 TOTAL:",total)
                        print ("Trabajador:",T,"\tSueldo: ",s)
                        total = total +1
                        TOTAL_SUELDOS= sueldos * total
                        print ("TOTAL SUELDOS:",TOTAL_SUELDOS)
                        break
                    elif s == 0:
                        print("NO EXISTE TRABAJADOR CON ESE SUELDO")
                
                    
def ver_estadisticas():
    print("\tESTADISTICAS")
    while True:
        try:
            for sueldo_alto in len(str(sueldos)):
                if sueldo_alto <= 2500000:
                    print("Sueldo más alto:",sueldo_alto)    
            for sueldo_bajo in len(str(sueldos)):
                if sueldo_bajo <= 800000:    
                    print("Sueldo más bajo:",sueldo_bajo)
            for promedio in len(str(sueldos)):
                if promedio == len(str(sueldos)):
                    print("Promedio de sueldos:", promedio)
            for media in sueldos:
                    media = (sueldos*10)**1/10
                    print("Media geométrica:",media)
        except:
            print("NO HAY SUELDO DISPONIBLE PARA LOS TRABAJADORES...INGRESE SUELDOS EN LA OPCIÓN 1")
            break
def reporte_sueldos():
    print("\tREPORTE DE SUELDOS"+".csv")
    while True:
            for T in trabajadores:
                print("Trabajador:",T,"\nSueldo base:",sueldos,"Descuento Salud:",SALUD,"Descuento AFP:",AFP,"Sueldo liquido:",SUELDO_LIQ)
                AFP=sueldos*12/100
                SALUD=sueldos*7/100
                SUELDO_LIQ=sueldos-AFP-SALUD
                with open ("REPORTE DE SUELDOS.csv", "w",newline="")as archivo:
                    escritor = csv.writer(archivo)
                    escritor.writerow(sueldos)
                    print("ARCHIVO CSV CREADO CON ÉXCITO")
def salir():
    print("Finalizando Programa...")
    print("Desarrollado por José Espinosa")
    print("RUT :20.037.942-K")
    exit()