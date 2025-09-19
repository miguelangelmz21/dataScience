#en este ejmplo el programa pedira la hora en formato de 24 e indicara
#el saludo correspondiente

hora=int(input('Ingresa solo la hora en formato de 24h: '))
#usaremos if anidados, es decir uno dentro de otro
if hora>=0 and hora<=24: #primer if, si la hora esta eb el rango de 0 y 24 entra
    if hora<7:
        print('es de madrugada...')
    elif hora<12:
        print('Buenos dias...')
    elif hora<19:
        print('Buenas tardes...')
    elif hora<=24:
        print('Buenas noches...')
else: #este else es del primer if
    print('Esa hora no existe...')