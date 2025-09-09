import pandas as pd
import matplotlib.pyplot as plt
#leemos el csv
archivo='calificaciones.csv'
datos=pd.read_csv('calificaciones.csv',encoding='utf-8')
#si guardaste el archivo con Excel, prueba estas codificaciones alternas
#datos=pd.read_csv('calificaciones.csv',enconding='latin1')
print('los datos son:\n',datos)
##crearemos un gráfico de barras
plt.figure(figsize=(8,6))
plt.bar(datos['Materia'],datos['Promedio'],color='lightgreen')
#añadir titulos y etiquetas
plt.title('Promedios de Calificaciones por Materias')
plt.xlabel('Materias')
plt.ylabel('Promedios')
#guardamos el gráfico
plt.savefig('promedioCalif.jpg')
#mostramos el gráfico
plt.show()