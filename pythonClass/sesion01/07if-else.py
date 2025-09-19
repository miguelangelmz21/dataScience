#veremos si un alumno está reprobado o aprobado, usando if - else

nota=float(input('Ingresa tu calificación final: '))
#evaluamos con la estructura selectiva if-else
if nota>=11:#si lo que hay en nota es mayor o igual a 11, entonces
    print('Felicitaciones, has aprobado el curso...')
else:#cuando no se cumpla la condición
    print('Lo sentimos, reprobaste el curso...')