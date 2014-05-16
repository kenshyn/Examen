import readline

class DataBase:
    def __init__(self, ruta="../database/apps.txt"):
        self.ruta = ruta


    def afegeixApp(self,nombre,proveedor,fecha,precio,numdesc,numpunt,punt,numcoment):
        added = False
        with open(self.ruta, 'a') as f:
            f.write(nombre+","+proveedor+","+fecha+","+str(precio)+","+str(numdesc)+","+str(numpunt)+","+str(punt)+","+str(numcoment)+"\n")
            added = True
        return added
    def llegeixApps(self,varllista):
        i=0
        resultat = ""
        listavar=list()
        with open(self.ruta, 'r') as f:
          for line in f:
            llistaresultat = line.split(",")
            if(varllista == "0"):
                if(llistaresultat[3] == "0"):
                    floatdescarga=float(llistaresultat[4])*0.6
                    floatpunt=float(llistaresultat[6])*0.25
                    floatcomentario=float(llistaresultat[7])*0.15
                    punt=floatdescarga+floatpunt+floatcomentario
                    listavar.append((str(punt),llistaresultat[0]))
                    i=i+1

            else:
                if(not(llistaresultat[3] == "0")):
                    floatdescarga=float(llistaresultat[4])*0.6
                    floatpunt=float(llistaresultat[6])*0.25
                    floatcomentario=float(llistaresultat[7])*0.15
                    punt=floatdescarga+floatpunt+floatcomentario
                    listavar.append((str(punt),llistaresultat[0]))
                    i=i+1


            sorted(listavar, key=lambda App: listavar[0])
        for item in listavar:
            print (item[1])

    def modificaApp(self, nombre, numerocambio):
        appList = []
        ibanExists = False
        with open(self.ruta, 'r') as accounts:
            for line in accounts:
                app = line.split(",")
                if(app[0] == nombre):
                    app[numerocambio] = str(float(app[numerocambio]) + 1)
                    changedLine = ','.join(app)
                    appList.append(changedLine)
                else:
                    appList.append(line)
            with open(self.ruta, 'w') as accounts:
                for item in appList:
                    if(item != ''):
                        accounts.write(item)

    def llegeixAppsperProveedor(self,varllista):
        i=0
        listavar=list()
        with open(self.ruta, 'r') as f:
          for line in f:
            llistaresultat = line.split(",")
            if(llistaresultat[1] == varllista):
                floatdescarga=float(llistaresultat[4])*0.6
                floatpunt=float(llistaresultat[6])*0.25
                floatcomentario=float(llistaresultat[7])*0.15
                punt=floatdescarga+floatpunt+floatcomentario
                listavar.append((str(punt),llistaresultat[0]))
                i=i+1
        sorted(listavar, key=lambda App: listavar[0])
        for item in listavar:
            print (item[1])
