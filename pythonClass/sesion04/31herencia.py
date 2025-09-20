#mostraremos cómo se comporta la herencia en python
#crearemos la super clase, o clase base o clase padre
class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def comer(self):
        print(f'{self.nombre} está comiendo...')#hasta aqui no hay herencia

#crearemos la sub clase, clase derivada o clase hija
class Perro(Animal):#la clase Perro hereda de la super clase Animal
    #pondremos un atributo heredado(nombre) y uno local(raza)
    def __init__(self,nombre,raza):
        super().__init__(nombre)#declaración del atributo heredado
        self.raza=raza#declaración del atributo local
    def ladrar(self):
        print(f'{self.nombre} es de la raza {self.raza}y está ladrando')

#crearemos el objeto de clase Perro
print('Crearemos el objeto miPerro de clase Perro\n'
      'que hereda atributos de la super clase Animal\n'
      'su nombre será Simba y su raza, labrador\n')
miPerro=Perro('Simba','Labrador')
miPerro.comer()#éste método es de la super clase
miPerro.ladrar()#éste método es de la sub clase