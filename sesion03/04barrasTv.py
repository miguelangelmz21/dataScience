import pandas as pd
import matplotlib.pyplot as plt
#cargamos el archivo
datos=pd.read_csv('ventas_televisores.csv')
#mostramos los datos
print('Los datos son:\n',datos)
#definimos el tamaño del gráfico
plt.figure(figsize=(10,6))
#Creamos las barras para cada mes y marca, la unidad (de la barra) es relativa dentro del sistema
#de coordenadas del eje X que se usa en el gráfico
bar_width=0.25#indicamos el ancho de cada barrita del gráfico
meses=datos['Mes']#guardamos una lista con los datos de la columna Mes
indices=range(len(meses))#guardamos la longitud de esta columna (la columna meses)
#crearemos las barras del gráfico
#creamos primero la barra de en medio
#creamos las barras de la marca samsung
samsung_bars=plt.bar(indices,datos['Samsung'],width=bar_width,label='Samsung',color='g')

#creamos las barras de la marca lg
lg_bars=plt.bar([i-bar_width for i in indices],datos['LG'],width=bar_width,label='LG',color='b')
#creamos las barras de la marca Sony
sony_bars=plt.bar([i+bar_width for i in indices],datos['Sony'],width=bar_width,label='Sony',color='#cc0000')

#añadimos titulos y etiquetas
plt.title('Ventas de Televisores por Marcas')
plt.xlabel('Meses')
plt.ylabel('Ventas')
#colocamos etiquetas de los meses en el eje x
plt.xticks(indices,meses)
#añadimos la leyenda
plt.legend()
#agregamos la cuadrícula
plt.grid(True,axis='y')
plt.show()
