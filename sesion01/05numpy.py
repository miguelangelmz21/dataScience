#ejemplo aplicado en ciencia de datos (normalización y estandarización)
import numpy as np
#supongamos que tenemos estas calificaciones
calificaciones=np.array([15,17,19,20,12])
print('Calificaciones originales:',calificaciones)
#normalización (escalar entre 0 y 1)
calificaciones_norm=(calificaciones-calificaciones.min())/(calificaciones.max()-calificaciones.min())
print('Calificaciones normalizadas:',calificaciones_norm)
#Estandarización (media=0, desviacion estándar=1)
calificaciones_std=(calificaciones-calificaciones.mean())/calificaciones.std()
print('Calificaciones estandarizadas:',calificaciones_std)