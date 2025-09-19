#uso de la estructura selectiva if, en su versión más simple
#pediremos el nombre y la edad del usuario y avisaremos si puede votar
nombre=input('Escribe tu nombre: ')
edad=int(input('Escribe tu edad: '))
#aqui viene la estructura selectiva if
if edad>=18: #si lo que hay en la variable edad es mayor o igual a 18 entonces
    print(f'{nombre} tienes {edad} años, si puedes votar')