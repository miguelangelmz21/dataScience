#crearemos una clase y un objeto normales para ejemplificar la creación
#de librerias
import pooLib33



class UsuariosPremium(pooLib33.Usuario):
    def __init__(self,id,alias,nombre,apellidos,sorteos,puntos):
        super().__init__(id,alias,nombre,apellidos)
        self.sorteos=sorteos
        self.puntos=puntos
    
    def muestra_datos(self):#este método es nuevo
        super().muestra_datos()#es de pooLib33 y solo muestra 4 datos
        print(f'Tienes {self.puntos} puntos para canjear en premios')
        print(f'Tienes derecho a participar en {self.sorteos} sorteos')

#crearemos la instancia de un objeto de clase UsuariosPremium
id=input('ID del Usuario: ')
alias=input('Alias: ')
nombre=input('Nombre: ')
apellidos=input('Apellidos: ')
sorteos=25
puntos=500
userPremium=UsuariosPremium(id,alias,nombre,apellidos,sorteos,puntos)
userPremium.muestra_datos()