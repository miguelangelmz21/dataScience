import pandas as pd
import matplotlib.pyplot as plt
#Muestra una lista de estilos prediseñados que podemos aplicar a los gráficos
#para cambiar su apariencia (ejemplo: 'ggplot','seaborn',etc)
print(plt.style.available)
#creamos un dataframe ficticio
data={
    'Año':[2016,2017,2018,2019,2020,2021],
    'Ventas':[250,300,400,350,500,450],
    'Ganancias':[50,80,100,90,120,110]
}

df=pd.DataFrame(data)
#usaremos un estilo alternativo usando 'ggplot' inspirado en el paquete
#ggplot2 de R.
plt.style.use('ggplot')
plt.figure(figsize=(10,6))
#usaremos plt.plot para graficar las ventas por año
#dividimos en 3 filas, con una columna cada fila, usamos la primera fila
plt.subplot(3,1,1) 
plt.plot(df['Año'],df['Ventas'],marker='o', linestyle='-',color='blue',label='Ventas')
plt.title('Ventas a lo largo de los años')
plt.xlabel('Años')
plt.ylabel('Ventas')
plt.grid(True)
plt.legend()

#2. Gráfico de barras
plt.subplot(3,1,2)#usaremos la segunda fila de las 3, el 1 es porque solo tienen una columna
plt.bar(df['Año'],df['Ganancias'],color='green',label='Ganancias')
plt.title('Ganancias por Año')
plt.xlabel('Años')
plt.ylabel('Ganancias')
plt.legend()

#3. histograma
plt.subplot(3,1,3)
#plt.hist crea un histograma para analizar la distribución de las ganancias
#df['Ganancias'] datos que se agruparán en el intervalo (bins)
#bins=5 divide los datos en 5 intervalos
#color cambia el color de la barra
#edgecolor pone un color de bordo a la barra
#alpha indica un grado de transparencia
plt.hist(df['Ganancias'],bins=5,color='purple',edgecolor='black',alpha=0.7)
plt.title('Distribución de ganancias')
plt.xlabel('Ganancias')
plt.ylabel('Frecuencias')
plt.tight_layout()#para que no se traslapen o se encimen los gráficos
plt.show()

