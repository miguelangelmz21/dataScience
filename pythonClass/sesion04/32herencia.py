#crearemos una super clase llamada figura con un atributo color y
#un método dibujar
class Figura:
    def __init__(self,color):
        self.color=color
    
    def dibujar(self):
        print(f'Estamos dibujando una figura de color: {self.color}')

#crearemos la subclase llamada Rectángulo que hereda de figura
class Rectangulo(Figura):#Rectangulo hereda de Figura
    def __init__(self,color,ancho,alto):
        #el atributo color se inicializa en la super clase
        super().__init__(color)
        self.ancho=ancho
        self.alto=alto
    #definimos la funcion calcular_area
    def calcular_area(self):
        return self.alto*self.ancho
    
#crearemos otra subclase llamada Circulo que hereda también de figura
class Circulo(Figura):
    def __init__(self,color,radio):
        super().__init__(color)
        self.radio=radio
    
    def calcular_area(self):
        return 3.1415*(self.radio**2)
#comienza el código del programa
#construimos los objetos
miRectangulo=Rectangulo('Azul',9.3,13.9)
miCirculo=Circulo('Amarillo',21.7)
#usaremos los métodos del objeto miRectangulo
miRectangulo.dibujar()
print('El área del rectángulo es:',miRectangulo.calcular_area())
#usaremos los métodos del objeto miCirculo
miCirculo.dibujar()
print('El área del círculo es:',miCirculo.calcular_area())