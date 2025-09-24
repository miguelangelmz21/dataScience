#Gráficos geográficos con Folium
#Mapa interactivo con marcadores para las ventas por ciudad
#pip install folium --user

import pandas as pd
import folium

# Cargar los datos
ventas_ciudades = pd.read_csv('ventas_ciudades.csv')

# Crear el mapa
mapa = folium.Map(location=[19.4326, -99.1332], zoom_start=5)
#folium.Map: Esta línea crea un mapa interactivo utilizando la biblioteca folium.
#location: Este parámetro define el punto central del mapa. Está definido como 
# una lista de coordenadas [latitud, longitud]. En este caso, las coordenadas 
# [19.4326, -99.1332] corresponden a la Ciudad de México.
#zoom_start: Establece el nivel de zoom inicial del mapa. Un valor de 5 es 
# un zoom relativamente alejado, que permite ver una región más amplia del mapa. 
# Puedes ajustar este valor para acercar o alejar la vista del mapa según tus 
# necesidades.

# Añadir marcadores
for index, row in ventas_ciudades.iterrows():
    #Esta línea inicia un bucle for que itera sobre cada fila del DataFrame 
    # ventas_ciudades. index es el índice de la fila actual. row es un objeto que 
    # contiene los datos de la fila actual.
    folium.Marker([row['Latitud'], row['Longitud']], 
                  popup=f"{row['Ciudad']} ventas: {row['Ventas']} ").add_to(mapa)
    # folium.Marker: Crea un marcador en el mapa en la ubicación especificada.
    #[row['Latitud'], row['Longitud']]: Especifica la ubicación del marcador usando 
    # las coordenadas de latitud y longitud de la fila actual del DataFrame.
    # popup=f"{row['Ciudad']}: {row['Ventas']} ventas"
    # popup: Este parámetro define el contenido que se mostrará cuando el usuario 
    # haga clic en el marcador. Aquí, se utiliza una f-string (f"{...}") para crear 
    # un texto que combina el nombre de la ciudad (row['Ciudad']) y el número de ventas 
    # (row['Ventas']) de esa ciudad. Por ejemplo, si la ciudad es "México" y las ventas 
    # son 1500, el popup dirá "México: 1500 ventas". add_to(mapa): Añade el marcador al 
    # objeto mapa que se creó anteriormente. Cada marcador se añade de forma secuencial 
    # para cada fila del DataFrame.

# Guardar el mapa en un archivo HTML
mapa.save('mapa_ventas_ciudades.html')
mapa