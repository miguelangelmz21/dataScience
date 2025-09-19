#veremos si un número es par o impar usando if - else
numero=int(input('Ingresa un número: '))
if numero%2==0:#si al dividir numero/2 el residuo (decimal) es 0 entonces
    print('El número es par...')
else:#en caso que no se cumpla la condición
    print('El número es impar...')