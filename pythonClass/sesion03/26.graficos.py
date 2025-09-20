#crearemos otro programa con interfaz gráfica
#importaremos la librería tkinter y la llamaremos tk
import tkinter as tk
#importamos la clase messagebox
from tkinter import messagebox

#crearemos una función que manejará una ventan con cuadros de diálogo
#y etiquetas
def etiquetas_y_texto():
    #crearemos la ventana
    ventana=tk.Tk()# el objeto Tk() crea la ventana
    ventana.title('Etiquetas y cuadros de texto')
    #ajustaremos el tamaño de la ventana
    ventana.geometry('400x250')
    #crearemos una etiqueta personalizada, gracias al objeto Label
    etiqueta=tk.Label(ventana,text="Ingresa tu nombre:",
                      font=("Arial",12,"bold"),fg="Blue")
    #empaquetaremos la etiqueta, con una separación en el eje y de 5 puntos
    etiqueta.pack(pady=5)
    #crearemos un cuadro de texto personalizado, es como un input
    entrada=tk.Entry(ventana,font=('Arial',12),width=30,justify='center')
    entrada.pack(pady=5)
    #crearemos una función para mostrar el nombre introducido
    #esta función estará dentro de la función anterior
    def mostrar_nombre():
        #obtendremos lo que hay en entrada (get) y eliminamos los
        #espacio del inicio y final del texto (strip)
        nombre=entrada.get().strip() 
        if nombre:#si hay información en la variable nombre, entonces
            messagebox.showinfo('Nombre:',f'Tu nombre es: {nombre}')
        else:#si no hay información en la variable nombre
            messagebox.showwarning('Advertencia','Por favor ingresa tu nombre')
    #crearemos otra función
    def borrar_texto():
        entrada.delete(0,tk.END)#elimina todo el contenido del entry
    #crearemos un frame para agrupar y centrar los botones dentro de ventana
    marco_botones=tk.Frame(ventana)
    marco_botones.pack(pady=10,expand=True)
    marco_botones.pack(pady=10,anchor='center')#centramos el frame en la ventana
    #botón para mostrar el texto
    boton_mostrar=tk.Button(marco_botones,text='Mostrar',font=('Arial',12),
                            #color de fondo verde, texto blanco, cuando se de clic al 
                            # botón, se ejecutará la función mostrar_nombre
                            bg='green',fg='white',width=10,command=mostrar_nombre)
    boton_mostrar.pack(side=tk.LEFT,padx=10)
    ventana.mainloop()
etiquetas_y_texto()
	