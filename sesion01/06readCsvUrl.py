import pandas as pd
print(pd.__version__)
#cargamos el dataset
url="https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
#cargamos un archivo csv en una variable gracias a pandas
df=pd.read_csv(url)
#mostramos los datos
print('Dataset original (primeras 5 filas):')
print(df.head())#.head() muestra los 5 primeros registros
input('Presiona enter para continuar\n')
#mostraremos los 5 ultimos registros del archivo
print('5 ultimas filas del dataset original:')
print(df.tail())#.tail() muestra los 5 ultimos registros
input('Presiona enter para continuar\n')
#mostraremos los primeros y ultimos registros
print('Normalmente muestra los primeros y últimos registros')
print(df)
input('Presiona enter para continuar\n')
#configuración para mostrar todas las filas de datos
pd.set_option('display.max_rows',None)
print('Estos son todos los registros del origen de datos')
print(df)
input('Presiona enter para terminar.')
#no olvides volver a ponerlo en su estado natural
pd.reset_option('display.max_rows',None)#regresa a su config. original