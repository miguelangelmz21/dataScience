import pandas as pd
import matplotlib.pyplot as plt
gapminder=pd.read_csv('gapminder.csv')

#crearemos un gráfico de dispersión
scatter=plt.scatter(
#los valores de la columna 'lifeExp' se ubican en el eje x
    gapminder['lifeExp'],
#los valores de la columna 'pop' se ubican en el eje y
    gapminder['pop'],
#los puntos se colorean en función de la esperanza de vida
    c=gapminder['lifeExp'],
#la paleta de colores es viridis, usa graduaciones del azul al amarillo
    cmap='viridis',
#0.7 hace los puntos ligeramente transparentes para mejorar la visibilidad
    alpha=0.7
)
#plt.colorbar:añade una barra lateral que muestra el rango de colores utilizados
plt.colorbar(scatter,label='Esperanza de vida')


plt.title('Relacion entre Esperanza de vida y población',fontsize=14)
plt.xlabel('Esperanza de vida',fontsize=12)
plt.ylabel('Población',fontsize=12)
plt.grid(True,linestyle='--',alpha=0.5)
plt.legend(['Esperanza de vida'],loc='upper left')
#para que no se superpongan los elementos
plt.tight_layout()
plt.show()