__author__ = 'Victor'
import datetime
from DataBase import *
import time

DataBase = DataBase()

print("Bienvenido a PeachStore!")
print("Que quieres hacer?")
print("1.- Listar aplicaciones")
print("2.- Añadir una nueva aplicacion")
print("3.- Modificar los datos de una aplicacion")
print("4.- Decargar la aplicacion")
print("5.- Comentar la aplicacion")
print("6.- Valorar la aplicacion")
print("7.- Calcular el dinero generado por una aplicacion")
print("8.- Listar las aplicaciones de un proveedor")
option = input("Selecciona una opcion: ")
if(option == "1"):
    opcionlista= input("Introduce 0 para listar aplicaciones gratuitas y 1 para aplicaciones de pago")
    DataBase.llegeixApps(opcionlista)
if(option == "2"):
    nombre = input("introduce el nombre de la app")
    proveedor = input("introduce su proveedor")
    fecha= time.strftime("%d/%m/%Y")
    print (fecha)
    precio = input("introduce su precio")
    numdesc = 0
    numpunt= 0
    punt = 0
    numcoment = 0
    result = DataBase.afegeixApp(nombre,proveedor,fecha,precio,numdesc,numpunt,punt,numcoment)
    if(result):
        print("App introducida correctamente")
    else:
        print("ha habido un error")
if(option == "3"):
    print("Funcion no implementada")
if(option == "4"):
    nombre = input("Que aplicacion quieres descargar?")
    DataBase.modificaApp(nombre, 4)
    print ("gracias por la descarga")
if(option == "5"):
    nombre = input("Que aplicacion quieres comentar?")
    DataBase.modificaApp(nombre, 7)
    print ("gracias por el comentario")
if(option =="6"):
    print("aun no")
if(option == "7"):
    print("nope")
if(option == "8"):
    nombreProv = input("Introduce el nombre del proveedor a mostrar")
    DataBase.llegeixAppsperProveedor(nombreProv)