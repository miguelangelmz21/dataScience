import pandas as pd
#simularemos un pequeño dataset 
data={
    'country':['USA','Perú','México'],
    'gdp_per_capita':[65000,10500,45000],
    'population':[331000000,126000000,380000000],
    'year':[2020,2021,2022]
}
df=pd.DataFrame(data)
print('El dataframe original es:\n',df)
#1. agregaremos una nueva columna 'Ingreso per cápita ajustado'
#este ajuste se hace por variaciones en la moneda, inflación, etc
df['Ingreso per cápita ajustado']=df['gdp_per_capita']/1.2
#2. Convertimos la columna year en tipo datetime
#usando pd.to_datetime para transformar los valores en objetos tipo fecha
df['year']=pd.to_datetime(df['year'], format='%Y')
#imprimimos el dataframe transformado
print('\nDataframe con las transformaciones:\n')
print(df)