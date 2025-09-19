#ejemplo de la estructura while
#simularemos el despegue de un cohete
import time
contador=10
print('Simularemos el conteo regresivo del despegue de un cohete')
while (contador>=0):#mientras contador sea mayor o igual a 0 haz lo siguiente
    time.sleep(1)#duerme el programa 1 segundo
    print(contador) #para ver horizontal print(contador,end=" ",flush=True)
    contador-=1#le quitamos 1 al valor de la variable contador
#aqui ya estamos fuera del ciclo
print('El cohete ha despegado...')
