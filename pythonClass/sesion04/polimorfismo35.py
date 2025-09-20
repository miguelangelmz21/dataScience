#crearemos la super clase Animal, con el encabezado de una función, o 
# método pero sin el cuerpo, similar a las interfaces en java

class Animal:#creamos la clase Animal
    def comunicarse(self):#solo tenemos el encabezado del método comunicarse
        raise NotImplementedError('La subclase, debe implementar el '
                                  'cuerpo del método comunicarse()')

#crearemos las subclases que heredarán el método comunicarse pero 
#deben implementar su código de diferente forma, según les convenga
#es decir, harán polimorfismo
class Perro(Animal):
    def comunicarse(self):
        return 'Soy un perro y ladro, Guuaaaauu!!!'

class Gato(Animal):
    def comunicarse(self):
        return 'Soy un gato y maullo, Miiiaaauuu!!!'

class Oso(Animal):
    def comunicarse(self):
        return 'Soy un oso y gruño Ggrrrrr!!!'
    
#como tenemos varios objetos, con método comunes, podemos meterlos en una 
# lista
animales=[Perro(),Gato(),Oso()]
#vamos a recorrer la lista
for animal in animales:#la variable animal, recorre la lista animales
    print(animal.comunicarse())
    input('Presiona enter para continuar...')    