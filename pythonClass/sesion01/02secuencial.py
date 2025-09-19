#veremos un programa con estructura secuencial, este programa
#tiene entrada de datos, procesamiento de datos y salida de datos
#el programa pide la base y la altura de un triangulo y calcula 
#su área
base=float(input('Ingresa la base del triangulo: '))
altura=float(input('Ingresa la altura del triangulo: '))
#procesamiento de datos
area=(base*altura)/2
#salida de datos
#mostraremos la información (el área del triangulo)
print('El área del triángulo es:',round(area,3))