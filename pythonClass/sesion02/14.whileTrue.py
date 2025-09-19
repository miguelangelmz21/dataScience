#veremos cómo validar una contraseña usando while True
usuario=input('Escribe tu usuario: ')
intentos=0
while True:
    password=input('Escribe tu contraseña: ')
    intentos+=1
    if password=='secreto123':
        print('Acceso correcto')
        break
    elif intentos==3:
        print('Se acabaron tus intentos')
        break
    else:
        print(f'LLevas {intentos} intentos')