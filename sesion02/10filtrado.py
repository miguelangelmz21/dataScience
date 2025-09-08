import pandas as pd
#cargamos un dataset
url="https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
df=pd.read_csv(url)

print('Dataset original (5 primeras filas):')
print(df.head())
input('Presiona enter para continuar\n')
#seleccionamos las filas donde 'life_expectancy'>70
df_filtro_esperanza_vida=df[df['lifeExp']>70]
print('Filas (5 primeras) donde la esperanza de vida es mayor a 70:')
print(df_filtro_esperanza_vida)
input('Presiona enter para continuar...\n')
#filtraremos y seleccionamos las columnas contry y year
df_columnas_seleccionadas=df_filtro_esperanza_vida[['country','year','lifeExp']]
print('\nFlitrado y selección de columnas contry, year y lifeExp (primeras filas)')
print(df_columnas_seleccionadas.head())
input('Presiona enter para continuar\n')
#mostrar todos los datos del filtro esperanza de vida
pd.set_option('display.max_rows',None)
#establece la opcion que nos permite desplegar el máximo
#de filas que hay 
print(df_filtro_esperanza_vida)
input('Presiona enter para continuar\n')
# mostrar solo un rango específico
print('Muestra los 10 primeros registros')
print(df_filtro_esperanza_vida.iloc[0:10])
input('Presiona enter para continuar\n')
#guardar la consulta en un archivo local de mi computadora
df_filtro_esperanza_vida.to_csv('filtrado_esperanza_vida.csv',index=False)
print('Archivo guardado como: filtrado_esperanza_vida.csv')