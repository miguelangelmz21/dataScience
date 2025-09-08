#un archivo csv es un archivo separado por comas u otro caracter similar
#y se puede usar en excel, bloc de notas y otros editores
import csv
#datos para crear el archivo csv
datos=[['Leche',5,28],
    ['Azucar',15,32],
    ['Arroz',23,30],
    ['Queso',14,140],
    ['Jamon',25,50]
]
#estructura para crear archivos
# with open('sesion02/productos.csv','w',newline='') as file:
with open('productos.csv','w',newline='') as file:
    #abre un archivo para escritura
    writer=csv.writer(file)
    #escribe los titulos o encabezados del archivo
    writer.writerow(['Productos','Cantidades','Precios'])
    #escribe los datos del archivo
    writer.writerows(datos)
print('\nEl archivo se creó con el nombre: productos.csv')