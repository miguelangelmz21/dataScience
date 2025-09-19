#veremos un ejemplo del uso de if estructurado if-elif-else
#pediremos la calificación de un alumno y la clasificaremos 
#si la calificación está entre 20 y 18 avisa Excelente calificación
#si la calificación está entre 15 y 17 avisa Buena calificación
#si la calificación está entre 11 y 14 avisa calificación suficiente
#si la calificación está entre 0 y 10 avisa Calificación no aprobatoria
nombre=input('Escribe tu nombre: ')
calificacion=float(input('Escribe tu calificación: '))
if calificacion<=20 and calificacion>=18:
    print(f'{nombre} tu calificación {calificacion} es excelente')
elif calificacion<18 and calificacion>=15:
    print(f'{nombre} tu calificación {calificacion} es buena')
elif calificacion<15 and calificacion>=11:
    print(nombre,'tu calificación',calificacion,'es suficiente')
elif calificacion<11 and calificacion>=0:
    print(nombre,'tu calificación',calificacion,'es reprobatoria')
else:#en cualquier otro caso
    print('Calificación no válida, ejecuta el programa otra vez...')