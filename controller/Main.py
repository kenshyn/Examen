__author__ = 'Victor'

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
if(option == 1):
    opcionlista= input("Introduce 0 para listar aplicaciones gratuitas y 1 para aplicaciones de pago")
    milista=