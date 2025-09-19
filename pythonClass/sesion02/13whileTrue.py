#veremos el uso de la estructura repetitiva while True
#el programa pedirá la palabra 'salir' para terminar el programa, 
# mientras esto no ocurra, seguirá pidiendo dicha palabra
while True:#mientras sea verdadero
    opcion=input('Escribe "salir" para terminar el ciclo: ')
    if opcion.lower()=='salir':#si lo que hay en la variable opción,
        #al convertirlo a minúsculas, es la palabra 'salir', entonces
        break#sal del ciclo
print('El programa ha terminado...')