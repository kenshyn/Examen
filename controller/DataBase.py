class DataBase:
    def __init__(self, ruta="../database/apps.txt"):
        self.ruta = ruta


    def afegeixApp(self,nombre,proveedor,fecha,precio,numdesc,numpunt,punt,numcoment):
        added = False
        with open(self.ruta, 'a') as f:
            f.write(nombre+","+proveedor+","+fecha+","+str(precio)+","+str(numdesc)+","+str(numpunt)+","+str(punt)+","+str(numcoment)+"\n")
            added = True
        return added