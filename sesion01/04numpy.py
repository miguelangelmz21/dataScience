#Estadística básica con numpy
import numpy as np
#crearemos un arreglo con valores aleatorios
arreglo=np.random.randint(1,100,size=10)
print('Arreglo con valores aleatorios:',arreglo)

#usaremos funciones estadísticas
print('Promedio:',np.mean(arreglo))
print('Mediana:',np.median(arreglo))
print('Varianza:',np.var(arreglo))
print('Desviación estandar:',np.std(arreglo))
#funciones matemáticas
print('Raíz cuadrada de cada elemento:',np.sqrt(arreglo))
print('Logaritmo natural de cada elemento',np.log(arreglo))