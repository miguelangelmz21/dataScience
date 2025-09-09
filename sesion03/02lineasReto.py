import pandas as pd
import matplotlib.pyplot as plt

#leemos el archivo csv
archivo='reto_academico.csv'
datos=pd.read_csv(archivo)
#mostramos el contenido
print('Los datos son:')
print(datos)
#crear el gráfico
plt.figure(figsize=(10,6))
#graficamos los datos de Carla
plt.plot(datos['Evaluación'],datos['Carla'],marker='o',label='Carla')
#graficamos los datos de Pedro
plt.plot(datos['Evaluación'],datos['Pedro'],marker='^',label='Pedro')
#graficamos los datos de Sofía
plt.plot(datos['Evaluación'],datos['Sofía'],marker='x',label='Sofía')
#añadimos etiquetas y titulos
plt.title('Rendimiento Académico')
plt.xlabel('Evaluaciones')
plt.ylabel('Calificaciones')
#agregamos la leyenda
plt.legend()
#agregamos la cuadrícula
plt.grid(True)
#guardaremos el gráfico como una imágen
plt.savefig('RendimientoAcademico.png')
#mostramos en pantalla
plt.show()
