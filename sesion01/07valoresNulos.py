import pandas as pd
#crearemos un pequeño dataframe con datos
data={
    'Nombre': ['Ana', 'Luis', 'Pedro', None],
    'Edad': [25, 30, None, 22],
    'Ciudad': ['Madrid', None, 'Barcelona', 'Valencia']
}

print('Los datos sin tratamiento son:')
print(data)
input('Presiona enter para continuar\n')

df=pd.DataFrame(data)#aqui convertimos los datos a dataframe
print('Dataframe original:')
print(df)
input('Presiona enter para continuar\n')

#identificar las celdas nulas
print('Celdas nulas identificadas:')
print(df.isnull())
input('Presiona enter para continuar\n')

#reemplazaremos valores nulos con valores predeterminados
df_reemplazo_pred=df.copy()#tomo una copia del dataframe original
#reemplazamos de la columna ciudad los nulos por la palabra desconocido
df_reemplazo_pred['Ciudad']=df_reemplazo_pred['Ciudad'].fillna('Desconocido')
#reemplazamos de la columna edad, los nulos, por el valor 0
#lo cual no siempre es lo óptimo porque te al tera tus calculos
df_reemplazo_pred['Edad']=df_reemplazo_pred['Edad'].fillna(0)
print('Dataframe con valores predeterminados en donde hay nulos')
print(df_reemplazo_pred)
input('Presiona enter para continuar\n')

#reemplazaremos los valores nulos en edad por el promedio de la columna
df_reemplazo_promedio=df.copy()
#calcula el promedio ignorando los nulos
promedio_edad=df['Edad'].mean(skipna=True)#se salta los nulos
#el promedio se calcula como (25+30+22)/3=25.6667
#ahora reemplazamos los nulos por el valor promedio calculado
df_reemplazo_promedio['Edad']=df_reemplazo_promedio['Edad'].fillna(promedio_edad)
print('Dataframe con valores nulos en la columna edad reemplazados por el promedio:')
print(df_reemplazo_promedio)
input('Presiona enter para continuar\n')

#eliminamos decimales en la columna edad
print('Dataframe con la columna edad formateada a 2 decimales:')
df_reemplazo_promedio['Edad']=df_reemplazo_promedio['Edad'].round(2)
print(df_reemplazo_promedio)
input('Presiona enter para continuar\n')

#agregamos una columna al dataframe, la columna estatura
df['Estatura'] = [1.78,1.80, None, 1.68]
print('Nuevo dataframe con estaturas:')
print(df)
