#crearemos una librería, para esto usaremos una clase normal
class Usuario:
    def __init__(self,id,alias,nombre,apellidos):
        self.id=id
        self.alias=alias
        self.nombre=nombre
        self.apellidos=apellidos
    
    def muestra_datos(self):
        print('Datos del Cliente:')
        print('Id:',self.id)
        print('Alias:',self.alias)
        print('Nombre:',self.nombre)
        print('Apellidos:',self.apellidos)
#probaremos, creando un objeto y usando su método, este código 
#se debe eliminar o comentar después de probar
# user=Usuario(13,'Fer','Fernando','Cruz Alvarez')#construimos un objeto
# user.muestra_datos()#probamos su método