#crearemos un ejemplo de interfaz gráfica usando la librería tkinter
import tkinter as tk #para crear interfaces gráficas
from tkinter import messagebox#para crear cajas de mensajes

#crearemos un método en el que estará todo el código de la interfaz
#gráfica
def ventana_con_boton():#definimos el método
    #crearemos la ventana principal
    ventana=tk.Tk()
    #pondremos título a la ventana
    ventana.title('Ejemplo con botón')
    #estableceremos el tamaño y posición de la ventana
    #(ancho x alto + posiniX + posiniY)
    ventana.geometry('400x300+400+200')
    #creamos un botón que se agrega al objeto ventana, con el texto "haz clic" y al presionarse
    #crea una caja de mensaje con el titulo mensaje y el texto "botón presionado"
    boton=tk.Button(ventana,text='haz clic',
                    command=lambda:messagebox.showinfo('Mensaje','Botón presionado'))
    #separa 20 pixeles al botón de otros componentes (en el eje y)
    boton.pack(pady=20)
    #mantiene la abierta esperando interacción con el usuario
    ventana.mainloop()
#invocamos al método ventana con botón
ventana_con_boton()