import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gapminder = pd.read_csv('gapminder.csv')
print('El dataframe original es:')
print(gapminder)
input('Presiona enter para continuar\n')
# Generación de datos ficticios para PIB si no está en gapminder
if 'PIB' not in gapminder.columns:
    #Fija la semilla para la generación de números aleatorios, 
    # asegurando que los resultados sean reproducibles.
    np.random.seed(42)
    #Genera números enteros aleatorios entre 1000 y 50000.
    #size=len(gapminder): La cantidad de números generados coincide 
    # con la cantidad de filas en el DataFrame.
    gapminder['PIB'] = np.random.randint(1000, 50000, size=len(gapminder))
print('El dataframe con PIB incluido es:')
print(gapminder)
input('Presiona enter para continuar\n')
# Cálculo de la matriz de correlación
corr_matrix = gapminder[['lifeExp', 'pop', 'PIB']].corr()
#Calcula la matriz de correlación, que mide la relación lineal entre las
#  variables seleccionadas:
#Valores cercanos a 1: Fuerte correlación positiva.
#Valores cercanos a -1: Fuerte correlación negativa.
#Valores cercanos a 0: Sin correlación significativa.

# Mapa de calor
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True)
#sns.heatmap:
#Crea un mapa de calor que visualiza la matriz de correlación.
#corr_matrix:
#Es la matriz de correlación que se utiliza como entrada.
#annot=True:
#Muestra los valores numéricos de las correlaciones en cada celda.
#fmt='.2f':
#Especifica el formato de los valores numéricos (dos decimales).
#cmap='coolwarm':
#Aplica el esquema de colores "coolwarm", que usa tonos azules y rojos para destacar 
# correlaciones negativas y positivas, respectivamente.
#cbar=True:
#Añade una barra lateral que muestra la escala de colores.
plt.title('Correlaciones entre Esperanza de Vida, Población y PIB', fontsize=14)
plt.tight_layout()
plt.show()