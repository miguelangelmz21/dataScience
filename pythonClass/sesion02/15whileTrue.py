#sumaremos números hasta que el usuario ingrese un cero
#al final el programa nos debe mostrar la suma de números introducidos
#y la cantidad de números que se sumaron
suma=0# irá guardando la suma de números introducidos
contador=0# irá contando cuantos números hemos introducido
while True:
    numero=float(input('Ingresa un número para sumarlo, (0 para salir): '))
    if numero==0:#si número es igual a 0, entonces
        break#salir del ciclo
    suma+=numero#suma guarda lo que ya tiene más el número que acaba de llegar
    contador+=1#incrementa cada que llega un número mientras no sea un cero
#fuera del ciclo
print('La suma de los números introducidos es:',suma)
print(f'El usuario introdujo {contador} números')