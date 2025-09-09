import pandas as pd
import matplotlib.pyplot as plt

#leer el archivo csv
archivo_csv='reto_dieta.csv'
datos=pd.read_csv(archivo_csv)

#mostrar el contenido del archivo csv
print(datos)

#crear gráfico de líneas
plt.figure(figsize=(10,6))

#graficar datos de Ana
# mes Es el eje X, datos['Ana'] es el eje Y, marcas: o,s,^,x,+
# label='Ana' nombre de la línea 
plt.plot(datos['Mes'],datos['Ana'],marker='o', label='Ana')
#graficar datos de Mario
plt.plot(datos['Mes'],datos['Mario'],marker='o',label='Mario')
#graficar datos de Luis
plt.plot(datos['Mes'],datos['Luis'],marker='o',label='Luis')

#Añadir titulos y etiquetas
plt.title('Evolución del Peso Durante la Dieta')
plt.xlabel('Mes')
plt.ylabel('Peso (Kg)')
#añadimos la leyenda
plt.legend()
#añadir cuadrícula
plt.grid(True)
#guardar el gráfico como un archivo de imagen
plt.savefig('evolucionPesoDieta.png')
#mostrar en pantalla
plt.show()
#etapas de la ciencia de datos
# cargar datos
#limpieza de datos
#transformación de datos
#estandarizar datos
#normalizar datos
#mostrar informacion (en forma de texto o en forma de gráficos)
#automatización y predicción de resultados (machine learning)