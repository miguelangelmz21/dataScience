#el objetivo de este ejercicio sencillo, es ver la potencialidad que tiene
#el machine learning para aprender de los datos que obtiene, en este caso
#le daremos información y le pediremos que aprende de los datos y genere 
#una formula que convierta de grados celcius a grados fahrenheit

#para construir y entrenar modelos de aprendizaje automático 
#y redes neuronales
import tensorflow as tf#pip install tensorflow
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#controlamos el uso de las optimizaciones de rendimiento de tensorflow
TF_ENABLE_ONEDNN_OPT=0
#importamos datos
temperaturaDF=pd.read_csv('celsius_a_fahrenheit.csv')
#vemos los datos
sns.scatterplot(data=temperaturaDF,x='Celsius',y='Fahrenheit')
plt.show()
#inicia el proceso de machine learning
#1. cargamos el set de datos en las variables de entrenamiento
X_train=temperaturaDF['Celsius']
y_train=temperaturaDF['Fahrenheit']
#creamos un modelo de red neuronal secuencial
#keras es un API de alto nivel que proporciona una manera sencilla de
#construir y entrenar redes neuronales
# 2 establecemos el modelo
model=tf.keras.Sequential()
#porqué Sequential? #se utiliza cuando los datos fluyen directamente de
#la entrada hacia la salida en un orden definido
#agregamos una capa de input solo creamos una neurona
# 3 creamos la capa de neuronas
model.add(tf.keras.layers.Dense(units=1,input_shape=[1]))
#el modelo tendrá una capa densa con 1 neurona y una entrada de 1 dimensión
model.summary()
input('Presiona enter para continuar')
#4 compilaremos el modelo
#llamamos al optimizador Adam (Adaptative Moment Estimation) que usa dos
#algoritmos: RMSProp: que mantiene una tasa de aprendizaje ajustada 
# automáticamente para cada parámetro
#Momentum: Acelera la convergencia acumulando información de gradientes
#anteriores
#0.5 es la tasa de aprendizaje (learning rate) ejemplos:
#Aprendizaje pequeño 0.001 es aprendizaje mas lento pero estable
#Aprendizaje grande 0.5 aprendizaje rápido pero con riesgo de no converger o saltar el óptimo
#loss='mean_squared_error' Define cómo medir el error entre las predicciones
#del modelo y los valores reales durante el entrenamiento
model.compile(optimizer=tf.keras.optimizers.Adam(0.5),
              loss='mean_squared_error')

#5 Entrenamos el modelo
#fit es el método que entrena el modelo
#en cada época el modelo realiza:
#un pase adelante(forward pass) para calcular predicciones
#un pase atrás(backward pass) para ajustar pesos usando el optimizador
#una época  es un pase completo por todo el conjunto de datos, cada vez
#que el modelo recorre los datos, ajusta sus pesos con base en los errores
#calculados
epochs_hist=model.fit(X_train,y_train,epochs=100)
#imprimiremos la pérdida cada vez
print(epochs_hist.history['loss'])
input('Presiona enter para continuar')

#Predicciones que hace nuestro modelo
#le damos temperaturas en grados celsius
temp_c=0
print('Si la temperatura en grados celsius es:',temp_c)
#el modelo nos predice
temp_f=model.predict(np.array([temp_c]))
#mostramos al usuario la temperatura que predice el sistema
print('Temperatura de predicción: '+str(temp_f))
#ahora aplicaremos la formula correcta para ver si coincide con
#la predicción del modelo
temp_f2=9/5*temp_c+32
print('Temperatura de la ecuación: '+str(temp_f2))
#ahora lo haremos con datos introducidos por el usuario
tempCUser=float(input('Escribe la temperatura en grados centígrados: '))
tempFModelo=model.predict(np.array([tempCUser]))
print('La temp. en grados Fahrenheit según el modelo es:',tempFModelo)
#calculamos con la fórmula
tempFFormula=9/5*tempCUser+32
print('La temp. en grados Fahrenheit según la fórmula es:',tempFFormula)
