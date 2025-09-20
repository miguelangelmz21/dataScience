#crearemos una clase que manipula información de vehiculos
#usaremos un método para imprimir su ficha técnica
class Vehiculos:
    def __init__(self,marca,tipo,modelo,color):
        self.marca=marca
        self.tipo=tipo
        self.modelo=modelo
        self.color=color
    
    def ficha_tecnica(self):
        print('\n---FICHA TÉCNICA DEL VEHICULO---\n')
        print('Marca:',self.marca)
        print('Tipo:',self.tipo)
        print('Modelo:',self.modelo)
        print('Color:',self.color)

#inicia el programa
vehiculo=Vehiculos('Toyota','Tacoma',2025,'Blanco')
vehiculo.ficha_tecnica()
marca=input('Escribe la marca de tu vehiculo: ')
tipo=input('Tipo del vehiculo: ')
modelo=input('Modelo del vehiculo: ')
color=input('Color del vehiculo: ')

vehiculo2=Vehiculos(marca,tipo,modelo,color)
vehiculo2.ficha_tecnica()