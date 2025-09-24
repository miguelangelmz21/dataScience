#PRECIOS VIVIENDAS
import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

#definimos nuestro conjunto de datos
house_df=pd.read_csv('precios_hogares.csv')
#visualizaremos los datos indicando X= tamaño de vivienda y=precio
sns.scatterplot(x='sqft_living',y='price',data=house_df)
plt.show()
#encontraremos la correlación
#definimos f y axis, los pondremos como subplots, definiremos 20
#crea una figura f y un conjunto de ejes(ax) para dibujar gráficos
f,ax=plt.subplots(figsize=(20,20))
#selecciona solo las columnas numéricas para calcular la correlación
numeric_cols=house_df.select_dtypes(include=[np.number])
#calcula la correlación
correlation_matrix=numeric_cols.corr()
#muestra el mapa de calor
sns.heatmap(correlation_matrix,annot=True)
plt.show()
##machine learning
#1 limpiamos los datos
#crearemos un set de entrenamiento y un set de prueba
selected_features=['bedrooms','bathrooms','sqft_living','sqft_lot',
                   'floors','sqft_above','sqft_basement']
#son los criterios a tomar en cuenta en el filtrado
#creamos la matriz de X
X=house_df[selected_features]#variables independientes
#lo que queremos predecir
y=house_df['price']#variable dependiente 
#######aqui en el ejemplo original va un gráfico si quieres lo pones después

#2 aplicaremos un escalado de datos
#pip install scikit-learn
from sklearn.preprocessing import MinMaxScaler
#crearemos una instancia del escalador MinMaxScaler
#es el objeto que realiza la transformación
scaler=MinMaxScaler()
#escalar es normalizar los datos a un rango específico, generalmente
#entre 0 y 1
X_scaled=scaler.fit_transform(X)

#3 normalizaremos nuestro output con reshape(-1,1):
#calcula automáticamente en una dimensión es decir en un array o vector
y=y.values.reshape(-1,1)
y_scaled=scaler.fit_transform(y)
#ya tenemos escalado al valor máximo de 1

#4 entrenamiento del modelo
from sklearn.model_selection import train_test_split
#toma los datos y los divide una parte para entrenamiento y una parte
#para prueba
#X_train,X_test,y_train,y_test son 4 tablas que guardaran los datos escalados obtenidos gracias 
#a la función train_test_split los obtiene de X_scaled y y_scaled
#25% de los datos los usará para probar
#y se probaran de manera aleatoria

X_train,X_test,y_train,y_test=train_test_split(X_scaled,y_scaled,test_size=.25,random_state=42)
# 5 definimos el modelo
model=tf.keras.models.Sequential()#usaremos el modelo sequencial
#recordemos que tiene 7 valores de entrada

# 6 creamos 3 capas con 100 neuronas
#keras es una api para crear redes neuronales
#units=100 la capa densa tiene 100 neuronas con 7 entradas
#cada neurona aplicará una trasnformación a los datos usando pesos y un sesgo, que se ajustan
#durante el entrenamiento
#activation='relu': (Rectified Linear Unit)  es una función de activación ampliamente usada en
#redes neuronales porque ayuda a introducir no linealidad en el modelo
#input_shape=7: especifica que se esperan 7 datos de entrada o variables
model.add(tf.keras.layers.Dense(units=100,activation='relu',input_shape=(7,)))
#creamos 2 capas más
model.add(tf.keras.layers.Dense(units=100,activation='relu'))
model.add(tf.keras.layers.Dense(units=100,activation='relu'))
#usaremos una sola neurona en la capa de salida (mostrará el precio)
model.add(tf.keras.layers.Dense(units=1,activation='linear'))
#vemos el resumen
model.summary()
input('Presiona enter para continuar...')
# 7 compilamos el modelo
#USARemos el optimizador Adam para compilar nuestro modelo
model.compile(optimizer='Adam', loss='mean_squared_error')

# 8 entrenamos nuestro modelo
epochs_hist=model.fit(X_train,y_train,epochs=100,batch_size=50, validation_split=0.2)
# 9 evaluamos el modelo
epochs_hist.history.keys()

#crearemos el grafico
plt.plot(epochs_hist.history['loss'])
plt.plot(epochs_hist.history['val_loss'])
plt.title('Progreso del modelo durante el entrenamiento')
plt.xlabel('Epoch')
plt.ylabel('Training and Validation Loss')
plt.legend(['Training Loss', 'Validation Loss'])
plt.show()

#haremos la predicción con sus entradas y salidas
#'bedrooms','bathrooms','sqft_living','sqft_lot','floors',
#'sqft_above=construccion','sqft_basement=sotano'

#asignaremos los valores para el hogar 
print('\nCalcularemos el costo de la casa que deseas\n')
recamaras=int(input('Numero de recamaras: '))
baños=int(input('Numero de baños: '))
constuccion=int(input('Pies cuadrados de construccion: '))
terreno=int(input('Pies cuadrados de terreno: '))
pisos=int(input('Numero de pisos: '))
superficie=int(input('Pies cuadrados sobre el nivel del suelo: '))
sotano=int(input('Pies cuadrados de sotano: '))
 
X_test_1=np.array([[recamaras,baños,constuccion,terreno,
                    pisos,superficie,sotano]])
#debemos escalar los valores en una escala de 0 a 1
scaler_1=MinMaxScaler()
X_test_scaled_1=scaler_1.fit_transform(X_test_1)
#haremos la prediccion
y_predict_1=model.predict(X_test_scaled_1)
#hasta el momento ya tiene el precio pero lo tiene escalado, lo queremos
#en formato real, haremos una transformación inversa de la escalacion
#revirtiendo el escalado
y_predict_1=scaler.inverse_transform(y_predict_1)
print('El costo de la vivienda con las características indicada es: '
      ,y_predict_1,'dolares')