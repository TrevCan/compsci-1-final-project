#!/usr/bin/python3 

import os


def espacios (longitud,cadena):
    
    espa = " " *(longitud - len(cadena))
    
    return espa


def listado_rango():
    
    val = 1
    
    rangoMin = input("Ingrese el promedio mínimo: ")
    
    while not rangoMin.isnumeric():
        input("Error. Valor debe ser número entero. [ENTER]")
        rangoMin = input("Ingrese el promedio mínimo: ")

    rangoMin = int(rangoMin)

    while rangoMin < 1 or rangoMin > 100:
        input("Error. Valor debe estar entre 1 y 100. [ENTER]")
        rangoMin = int(input("Ingrese el promedio mínimo: "))


    rangoMax = input ("Ingrese el promedio máximo: ")

    while not rangoMax.isnumeric():
        input("Error. Valor debe ser número entero. [ENTER]")
        rangoMax = input ("Ingrese el promedio máximo: ")

    rangoMax = int(rangoMax)

    while rangoMax < 1 or rangoMax > 100:
        input("Error. Valor debe estar entre 1 y 100. [ENTER]")
        rangoMax = int(input ("Ingrese el promedio máximo: "))

    
    archivo = open ("calificaciones.csv","r")
    
    for dato in archivo.readlines():
        
        dato = dato[:-1]
        
        ren_div = dato.split(",")
        
        if int(ren_div[5]) >= rangoMin and int(ren_div[5]) <= rangoMax:
        
            if val == 1:
                
                print()
            
                print ("Matrícula        Nombre           Apellido P       Apellido M       Carrera          Promedio")
            
                print ("---------------------------------------------------------------------------------------------")
                
                val = 2
            
            print ((ren_div[0] + espacios(17,ren_div[0]) + ren_div[1] + espacios(17,ren_div[1]) + ren_div[2] + espacios(17,ren_div[2]) + ren_div[3] + espacios(17,ren_div[3])+ ren_div[4] + espacios(17,ren_div[4]) + ren_div[5]))
            
            
    if val == 1:
        
        print()
        
        print("El rango elegido no existe en el sistema [ENTER]")
           
     
    archivo.close()
    
    input()    
        
def listado_carrera():
    
    val = 1
    
    cont = 0
    
    suma = 0
    
    carrera = input ("Ingrese la carrera: ")
    
    archivo = open ("calificaciones.csv","r")
    
    for dato in archivo.readlines():
        
        dato = dato[:-1]
        
        ren_div = dato.split(",")
        
        if carrera == ren_div[4]:
            
            cont = cont + 1
            
            suma = suma + int(ren_div[5])
            
            if val == 1:
                
                print()
            
                print ("Matrícula        Nombre           Apellido P       Apellido M       Carrera          Promedio")
            
                print ("---------------------------------------------------------------------------------------------")
                
                val = 2
            
            print ((ren_div[0] + espacios(17,ren_div[0]) + ren_div[1] + espacios(17,ren_div[1]) + ren_div[2] + espacios(17,ren_div[2]) + ren_div[3] + espacios(17,ren_div[3])+ ren_div[4] + espacios(17,ren_div[4]) + ren_div[5]))
            
    if cont >= 1:
        
        promedio = suma/cont
        
        print("\n"*2)
        
        print("------------------------------------------------------------")
        
        print ("El promedio de los alumnos listados es igual a: ", promedio)
        
        print("------------------------------------------------------------")
    
    else:
        
        print()
        
        print("No se encontró ningún alumno con la carrera ingresada.")
        
    archivo.close()
    
    print()
    
    input ("Presione [ENTER] para regresar al menú.")
    
    
def listado_paterno():
    
    val = 1
    
    apellido_p = input ("Ingrese el apellido paterno del estudiante cuyos datos desea conocer: ")
    
    archivo = open("calificaciones.csv","r")

    for dato in archivo.readlines():
        
        dato = dato[:-1]
        
        ren_div = dato.split(",")
        
        if apellido_p == ren_div[2]:
            
            if val == 1:
                
                print()
            
                print ("Matrícula        Nombre           Apellido P       Apellido M       Carrera          Promedio")
            
                print ("---------------------------------------------------------------------------------------------")
                
                val = 2
            
            print()
                    
            print (ren_div[0] + espacios(17,ren_div[0]) + ren_div[1] + espacios(17,ren_div[1]) + ren_div[2] + espacios(17,ren_div[2]) + ren_div[3] + espacios(17,ren_div[3])+ ren_div[4] + espacios(17,ren_div[4]) + ren_div[5])
            
                
    if val != 2 :
        
        print()
        
        print ("Apellido paterno no encontrado. Presione [ENTER] para volver al menú: ")

    input()
    
    archivo.close()
    
    

def listado():
    
    print ("\n"*20)
    
    print ("===============================================================")
    
    print ("Usted ha elegido la opción 'Listado de alumnos'.")
    
    print ("===============================================================")
    
    archivo = open("calificaciones.csv","r")
    
    print()
    
    print ("---------------------------------------------------------------------------------------------")
            
    print ("Matrícula        Nombre           Apellido P       Apellido M       Carrera          Promedio")
            
    print ("---------------------------------------------------------------------------------------------")

    
    for dato in archivo.readlines():
    
        dato = dato[:-1]
        
        ren_div = dato.split(",")
      
                
        print (ren_div[0] + espacios(17,ren_div[0]) + ren_div[1] + espacios(17,ren_div[1]) + ren_div[2] + espacios(17,ren_div[2]) + ren_div[3] + espacios(17,ren_div[3])+ ren_div[4] + espacios(17,ren_div[4]) + ren_div[5])
            
    
    archivo.close()
    
    input()


def consulta_matricula():
    
    val = False
    
    print ("\n"*20)
    
    print ("===============================================================")
    
    print ("Usted ha elegido la opción 'Consulta de alumnos por matrícula'.")
    
    print ("===============================================================")
    
    matricula = input ("Ingrese la matrícula del estudiante cuyos datos desea conocer: ")
    
    archivo = open("calificaciones.csv","r")
    
    for dato in archivo.readlines():
        
        dato = dato[:-1]
        
        ren_div = dato.split(",")
        
        if matricula == ren_div[0]:
            
            print()
            
            print ("Matrícula        Nombre           Apellido P       Apellido M       Carrera          Promedio")
            
            print ("---------------------------------------------------------------------------------------------")
            
            print (ren_div[0] + espacios(17,ren_div[0]) + ren_div[1] + espacios(17,ren_div[1]) + ren_div[2] + espacios(17,ren_div[2]) + ren_div[3] + espacios(17,ren_div[3])+ ren_div[4] + espacios(17,ren_div[4]) + ren_div[5])
            
            val = True
            
            input()
    
    if val == False:
        
        print()
        
        input ("Matrícula no encontrada. Presione [ENTER] para volver al menú: ")

    archivo.close()
    
    
def alta():
    
    x = True

    
    print ("\n"*20)
    
    print ("=============================================")
    
    print ("Usted ha elegido la opción 'Data de alumnos'.")
    
    print ("=============================================")
    
    
    while x == True:
        
        print ()
        
        matricula = input ("Ingrese la matrícula del estudiante (5 caracteres): ")
    
        if len(matricula) < 5 or len(matricula) > 5 or matricula.isalnum() != True:
            
            print()
            
            input ("Error, la matrícula no cumple con las especificaciones requeridas. Presione [ENTER]")
            
        else:

            if os.path.isfile("calificaciones.csv"):
                            
                archivo = open ("calificaciones.csv","r")
                
                existe = False
                
                for linea in archivo.readlines():
                    
                    linea = linea[:-1]
                    
                    linea_individual = linea.split(",")
                    
                    if matricula == linea_individual[0]:
                        
                        print()
                        
                        print ("Error, la matrícula ingresada ya se encuentra en el archivo.")
                        
                        x = False
                        
                        print()
                        
                        input ("Presiona [ENTER] para continuar: ")    
                    
            if x:
                    
                while x == True:
                    
                    nombre = input ("Indique el nombre del estudiante (máximo 15 caracteres): ")
                        
                    if len(nombre) < 1 or len(nombre) > 15:
                            
                        input ("Error, el nombre no cumple con las especificaciones requeridas. Presione [ENTER]")
                        
                    else:
                            
                        while x == True:
                            
                            apellido_paterno = input ("Indique el Apellido Paterno del estudiante (máximo 15 caracteres): ")
                                
                            if len(apellido_paterno) < 1 or len(apellido_paterno) > 15:
                                    
                                input ("Error, el apellido no cumple con las especificaciones requeridas. Presione [ENTER]")
                                
                            else:
                                    
                                while x == True:
                                    
                                    apellido_materno = input ("Indique el Apellido Materno del estudiante (máximo 15 caracteres): ")
                                        
                                    if len(apellido_materno) < 1 or len(apellido_materno) > 15:
                                            
                                        input ("Error, el apellido no cumple con las especificaciones requeridas. Presione [ENTER]")
                                            
                                    else:
                                            
                                        while x == True:
                                            
                                            carrera = input ("Indique la carrera universitaria del estudiante (3 caracteres): ")
                                                
                                            if len(carrera) < 3 or len(carrera) > 3:
                                                    
                                                input ("Error, la carrera universitaria no cumple con las especificaciones requeridas. Presione [ENTER]")
                                                    
                                            else:
                                                    
                                                while x == True:
                                                        
                                                    promedio = input ("Indique el promedio del estudiante (1-100): ")
                                                        
                                                    if promedio.isnumeric() == True:
                                                            
                                                        promedio = int(promedio)
                                                            
                                                        if promedio < 1 or promedio > 100:
                                                            
                                                            input ("Error, el promedio no cumple con las especificaciones requeridas. Presione [ENTER]")
                                                            
                                                        else:
                                                                
                                                            promedio = str(promedio)
                                                        
                                                            datos_alumno = matricula + "," + nombre + "," + apellido_paterno + "," + apellido_materno + "," + carrera + "," + promedio + "\n"
                                                                
                                                            archivo = open("calificaciones.csv","a")
                    
                                                            archivo.write(datos_alumno)
                                                                                
                                                            archivo.close()
                                                                
                                                            print()
                                                                
                                                            input ("Los datos se han guardado correctamente en la base de datos. Presione [ENTER] para regresar al menu: ")
                                                                
                                                            x = False
                                                       
            
                                                    else:
                                                            
                                                        input ("Error, el promedio debe ser numérico y entero.")
                                                        
                                                                                                           
                                                                                     
                                                                                                                                                                                              

def menu():
    
    opcion = 0
    
    while opcion != 7:
    
        print ("""
        MENÚ DE OPCIONES:
        

        1) Alta de alumnos.

        2) Consulta de alumnos por matrícula.

        3) Listado general de alumnos.

        4) Listado de Alumnos por Apellido Paterno.

        5) Listado de Alumnos por Carrera.

        6) Listado de Alumnos en rango de promedio.

        7) Terminar.

        """)
            
        opcion = input ("Ingrese la opción deseada: ")
        
        if opcion == "1":
            
            alta()
        
        elif opcion == "2":
            
            consulta_matricula()
            
        elif opcion == "3":
            
            listado()
            
        elif opcion == "4":
            
            listado_paterno()
            
        elif opcion == "5":
            
            listado_carrera()
            
        elif opcion == "6":
            
            listado_rango()
            
        elif opcion == "7":
            
            input ("Cerrando, presiona [ENTER] para salir.")
            
            break
            
        else:
            
            input("La opción ingresada no se encuentra en el sistema. Presione [ENTER]")
            
        
        
menu()

