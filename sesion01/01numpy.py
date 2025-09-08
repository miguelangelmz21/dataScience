#numpy es una librería que se especializa en el manejo de arreglos
#y operaciones matemáticas, así como la generación de números 
# pseudo aleatorios
import numpy as np
#craremos un arreglo unidimensional
arreglo=np.array([10,20,30,40,50])
print('Arreglo original: ',arreglo)
#operaciones básicas
print("La suma de todos los elementos:",arreglo.sum())
print('Valor máximo:',arreglo.max())
print('Valor mínimo:',arreglo.min())
print('Promedio:',arreglo.mean())
print('Desviación estándar:',arreglo.std())