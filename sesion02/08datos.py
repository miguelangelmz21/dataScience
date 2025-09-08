import pandas as pd
#cargaremos datos desde un archivo csv
# df=pd.read_csv('AExpDatVentas.csv')
df = pd.read_csv(r"C:\Users\PCHome\git-practic\DataScience\sesion02\AExpDatVentas.csv")
print('Los datos que contiene el dataframe son:\n',df)
input('Presiona enter para continuar\n')
#formateamos las fechas
df['Fecha de Venta']=pd.to_datetime(df['Fecha de Venta'])
#descripción estadística básica
descripcion=df
print(descripcion)
input('Presiona enter para continuar\n')
#calcular la cantidad total de productos vendidos
total_cantidad=df['Cantidad'].sum()
print('La cantidad de productos vendidos es:',total_cantidad)
mas_vendido=df['Cantidad'].max()
print('la cantidad máxima vendida es:',mas_vendido)
menos_vendido=df['Cantidad'].min()
print('La cantidad mínima vendida es:',menos_vendido)
input('Presiona enter para continuar\n')
###a partir de aquí corresponde a la transformación de datos de un dataframe
#calcularemos el total de ingresos por productos
df['Ingresos']=df['Precio']*df['Cantidad']
#calculamos el ingreso total sumando el contenido de la col ingresos
ingreso_total=df['Ingresos'].sum()
print('Ingreso total:',ingreso_total,'dolares')
print('\nAgregaremos las columnas: Impuesto y total')
#calculamos el impuesto
df['Impuesto']=df['Ingresos']*.18
df['Total']=df['Ingresos']+df['Impuesto']
print('El dataframe con el total es:\n',df)