#crearemos un programa que con base al peso dado de una persona
#emita un dictámen, si el peso es:
#>120 Tienes sobrepeso
#si está entre 120 y 90 eres corpulento
#si  está entre 89.999 y 70 eres fornido
#si está entre 69.999 y 50 estás en forma
#si está entre 49.999 y 40 eres delgado
#si es menor que 40 y hasta 20 kg Cuida tu salud
#en cualquier otro caso, avisar: Ese peso no es válido para personas normales
nombre=input('Escribe tu nombre: ')
peso=float(input('Escribe tu peso corporal en kg: '))
if peso>120  and peso <350:
    print('Tienes sobrepeso')
elif peso<120 and peso>=90:
    print('Eres corpulento')
elif peso<90 and peso>=70:
    print('Eres fornido')
elif peso<70 and peso>=50:
    print('Estás en forma')
elif peso <50 and peso >=40:
    print('Eres delgado')
elif peso<40 and peso >=20:
    print('Cuida tu salud')
else:
    print('Ese peso no es válido para personas normales...')