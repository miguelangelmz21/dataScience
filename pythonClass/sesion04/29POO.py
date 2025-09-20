#crearemos la clase Triangulo, con un función para calcular el área
class Triangulo:#creamos la clase
    #definimos el constructor
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    
    #definimos la función para calcular el área
    def area(self):
        #se llama función porque retorna un valor
        return(self.base*self.altura)/2
    
#inicia nuestro programa
base=float(input('Escribe la base del Triangulo: '))
altura=float(input('Escribe la altura del Triangulo: '))
#construiremos el objeto
triangulo=Triangulo(base,altura)
#invocaremos el método para calcular el área
print('El área del triangulo es:',triangulo.area())