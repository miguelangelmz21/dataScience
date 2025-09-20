#cuando necesitamos programa con el paradgima orientado a objetos, 
#todo lo debemos pensar como objetos con propiedades o características
#y eventos que se pueden realizar con esos objetos, por ejemplo si 
#el objeto es una botella de plástico, sus atributos pueden ser:
#material, color, tamaño, capacidad,etc y sus eventos serían:llenar 
#la botella, destapar la botella, vaciar la botella
# pero, para que exista una botella, debe haber antes un molde para 
# crear botellas, a ese molde en programación, le llamamos clase, es
# decir, una clase es un molde  para crear objeto de dicha clase
#paradigma imperativo
#aqui decimos qué hacer y cómo hacerlo 

import time
n=1
print('n vale',n)
#paradigma orientado a objetos
#se estructuran objetos con atributos y métodos y luego solo se invocan
#persona1=Persona(nombre,edad) #creas el objeto persona1 de clase Persona
#persona1.saludar()#invocas al metodo saludar de la clase persona1
#persona2=Persona(nombre,edad)
#persona2.saludar()

#paradigma funcional


####empezamos
#crearemos la clase Persona (molde para hacer objetos)
class Persona:#inciamos la clase Persona
    #parte privada del objeto (constructor de la clase)
    def __init__(self,nombre,edad):#inicializamos el constructor
        self.nombre=nombre
        self.edad=edad
    
    #parte pública del objeto(puede ser una función[si retorna un valor]
    #o un método [si no retorna un valor])
    def saludar(self):#inicia el método saludar
        print(f'Hola, mi nombre es: {self.nombre} y mi edad: {self.edad}')

#inicia nuestro programa, crearemos los objetos de la clase Persona
persona=Persona('Juan',25)
persona2=Persona('Ana',31)
print('Se construyeron 2 objetos, persona y persona2\n')
#accederemos a los atributos de estos objetos, de manera individual
print(f'Los datos del objeto llamado persona son: nombre {persona.nombre} edad:{persona.edad}')
print(f'Los datos del objeto llamado persona2 son: nombre {persona2.nombre} edad:{persona2.edad}')
#acceremos a los métodos de los objetos
persona.saludar()
persona2.saludar()