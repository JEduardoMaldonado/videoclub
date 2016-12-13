import json

class clien:  
    cli = []

    def read(self):
        with open('clientes.json','r') as file:
            cli = json.load(file)
            self.cli = cli['results'] 

    def getCliente(self): 
        clientes = []
        for row in self.cli:
            cliente = row['nombre']
            if cliente not in clientes:
                clientes.append(cliente)
        return clientes

    
                
class peli:  
    peli = []

    def read(self):
        with open('peliculas.json','r') as file:
            peli = json.load(file)
            self.peli = peli['results'] 

    def getPeliculas(self): 
        peliculas = []
        for row in self.peli:
            pelicula = row['nombre']
            if pelicula not in peliculas:
                peliculas.append(pelicula)
        return peliculas