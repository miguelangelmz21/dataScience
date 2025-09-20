#pip install mysql.connector
#C:\Users\PCHome>cd \xampp\mysql\bin
#C:\xampp\mysql\bin>mysql -h localhost -u root -p -P 3306
#MariaDB [(none)]> create database tiendaperu;
#MariaDB [(none)]> use tiendaperu;
#
#
#

'''Un CRUD es la base de cualquier sistema computacional
son las rutinas de Create (insertar datos) Read (leer datos)
Update (modificar datos) y Delete (eliminar datos)
si tienes un punto de ventas (Point Of Sale) 
Clientes, productos, ventas, pedidos, etc, para cada elemento
debes crear un CRUD'''

import os #para tareas del sistema operativo
import time
import mysql.connector
#si sigue subrayado pruebas esto: import mysql-connector
#1.
#crearemos el módulo que conectará python con la base de datos 
#de mysql
mybd=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='tiendaperu',
    port='3306'#si cambiaste el puerto, pon el número que usaste
)
#2. 
#crearemos un cursor (un objeto para ejecutar comandos en la base de datos)
mycursor=mybd.cursor()
#3. Crearemos un menú que verá el usuario, este será nuestro pequeño
#front end, como queremos que al menos lo vea 1 vez el usuario
while True:
    print('---MENU DEL SISTEMA---'
          '\n1. Agregar un producto al sistema'
          '\n2. Eliminar un producto del sistema'
          '\n3. Buscar  un producto en el sistema'
          '\n4. modificar  un producto en el sistema'
          '\n5. Mostrar el catálogo de productos del sistema'
          '\n6. Salir del sistema')
    opcion=int(input('Elige una opción del menú: '))
    #si el usuario elige la opción 1
    if opcion==1:#El usuario quiere guardar un nuevo producto (CREATE)
        #primero hay que pedir los datos del producto
        clave=int(input('Clave del producto: '))
        nombre=input('Nombre del producto: ')
        precio=float(input('Precio del producto: '))
        #creamos la instrucción para insertar
        sql='INSERT INTO productos (clave,nombre, precio) VALUES (%s,%s,%s)'
        #creamos la tupla (los datos) para insertar
        val=(clave,nombre,precio)
        #preparamos los datos para insertar
        mycursor.execute(sql,val)
        #insertamos
        mybd.commit()
        #avisamos al usuario
        print('Producto agregado al sistema...')
        time.sleep(2)
        os.system('cls')#linux o mac 'clear' para limpiar la pantalla
    elif opcion==2:#Eliminar un producto (DELETE)
        #primero hay que pedir la clave del producto
        clave=int(input('Ingresa la clave del producto a eliminar: '))
        #creamos la instrucción para eliminar
        sql='DELETE FROM productos WHERE clave=%s'
        #creamos la tupla
        val=(clave,)
        #creamos la instrucción para eliminar
        mycursor.execute(sql,val)
        #realizamos la eliminación
        mybd.commit()
        #avisamos al usuario que ya eliminamos el producto
        print(mycursor.rowcount,'Productos eliminados')
        time.sleep(2)
        os.system('cls')#clear linux o mac
    elif opcion==3:#Buscar un producto (READ)
        #debemos pedir la clave del producto a buscar
        clave=int(input('Escribe la clave del producto a buscar: '))
        #crearemos la consulta, en este caso es de selección
        sql='SELECT * FROM productos WHERE clave=%s'
        #creamos la tupla
        val=(clave,)
        #preparamos la instrucción
        mycursor.execute(sql,val)
        #verificaremos si existe el producto
        myresult=mycursor.fetchall()#devuelve los registros encontrados 
        if myresult:#si hay datos en myresult?
            print('El producto si existe en el sistema...')
        else:#si no hay resultados
            print('El producto no existe en el sistema...')
        time.sleep(2)
        os.system('cls')
    elif opcion==4:#modificar un producto (UPDATE)
        clave=int(input('Clave del producto a modificar: '))
        nombre=input('Nuevo nombre del producto: ')
        precio=float(input('Nuevo precio del producto: '))
        #crearemos la consulta de actualización
        sql='UPDATE productos SET nombre=%s, precio=%s WHERE clave=%s'
        #crearemos la tupla con los nuevos datos
        val=(nombre,precio,clave)
        #preparamos para la ejecución
        mycursor.execute(sql,val)
        mybd.commit()
        #le avisamos al usuario
        print('El producto se ha modificado correctamente.')
        time.sleep(2)
        os.system('cls')
    elif opcion==5:#consulta general (READ)
        #creamos la consulta general a la tabla productos
        mycursor.execute('SELECT * FROM productos')
        myresult=mycursor.fetchall()
        #mostramos el contenido de la tabla
        print('--CATALOGO DE PRODUCTOS---')
        for x in myresult:
            #imprimimos cada fila o registro de la tabla
            print(x)
        input('Presiona enter para continuar...')
        os.system('cls')
    elif opcion==6:#salir del sistema
        respuesta=input('Estas seguro? (s/n): ')
        if respuesta.upper()=='S':
            print('Saliendo del sistema...')
            time.sleep(2)#esto se ejecuta si quiere salir
            os.system('cls')
            break#salir del ciclo while True
        time.sleep(2)#esto se ejecuta si no quiere salir
        os.system('cls')
    else:#si la opción no es un número del 1 al 6
        print('Opción no válida, intenta de nuevo')
        time.sleep(2)
        os.system('cls')
mybd.close()#si no cerramos la base de datos, se fragmenta y se puede dañar