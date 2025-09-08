import pandas as pd
#los datos los puedes tomar de un csv o de internet o de excel o de 
#una base de datos
data = {
    'country': ['Germany','Italy','France','Argentina', 'Brazil', 'Chile', 'Argentina', 'Brazil', 'Chile','Germany','Italy','France'],
    'continent': ['Europe','Europe','Europe','South America', 'South America', 'South America', 'South America', 'South America', 'South America','Europe','Europe','Europe'],
    'year': [2000, 2000, 2000,2000, 2000, 2000, 2010, 2010, 2010, 2010, 2010, 2010],
    'life_expectancy': [72.2,74.3,69.5,75.3, 72.4, 77.1, 76.5, 73.2, 78.4,75.2,76.1,71.2]
}

print('Los datos en su formato original son:\n',data)
input('Presiona enter para continuar\n')
#creamos el dataframe
df=pd.DataFrame(data)
print('Los datos en formato DataFrame son:\n',df)
input('Presiona enter para continuar\n')
#1. crear una tabla dinámica con el promedio de vida 'life_expectancy'
#por 'continent' y 'year'
'''pd.pivot_table crea una tabla dinámica'''
pivot_avg=pd.pivot_table(df,# es el dataframe original
values='life_expectancy',# es la columna numérica que quieres agrupar
#y resumir
index='continent',#los valores únicos de la columna continent serán
#las filas de la tabla resultante
columns='year',#los valores únicos de la columna year serán las 
#columnas de la tabla
aggfunc='mean')#es la función de agregación que se aplicará a los datos
                #en este caso es la función promedio
print('Tabla dinámica con las esperanzas de vida promedio:')
print(pivot_avg)
input('Presiona enter para continuar\n')

#2. Modificamos la tabla dinámica para usar el máximo en lugar del promedio
#ahora queremos el máximo de esperanza de vida por continente y por año
pivot_max=pd.pivot_table(df,#el dataframe original
    values='life_expectancy',#columna numérica que se va a agrupar
    index='continent',#los valores únicos de continent serán las filas
    columns='year',#los valores únicos de year serán las columnas
    aggfunc='max')#la función de agregación ahora es max
print('Tabla dinámica con las esperanzas de vida máximas:')
print(pivot_max)
input('Presiona enter para continuar\n')


#3. Usaremos una función personalizada para calcular la moda
def mode_custom(series):
    #si hay multiples modas, toma solo la primera, en caso de que no estén vacias las modas, 
    #en caso contrario, no devuelvas nada
    return series.mode().iloc[0] if not series.mode().empty else None

#creamos una tabla pivote que muestre la moda de 'life expectancy' por 'continent' y 'year'
pivot_mode=pd.pivot_table(df,
    values='life_expectancy',
    index='continent',
    columns='year',
    aggfunc=mode_custom)
print('Tabla dinámica de la Moda analizando las esperanzas de vida')
print(pivot_mode)

