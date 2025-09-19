#Calcularemos el promedio de 3 calificaciones
import time
#entrada de datos
mat=float(input('Calificación de matemáticas: '))
fis=float(input('Calificación de física: '))
quim=float(input('Calificación de química: '))
#procesamiento de datos
promedio=(mat+fis+quim)/3
print('Procesando datos...')
time.sleep(3)
print(f'El promedio es: {round(promedio,2)}')