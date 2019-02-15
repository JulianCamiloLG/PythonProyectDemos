from cProfile import run
import random
import tkinter as tk
from tkinter import filedialog

nombres = ["julian", "camilo", "andres", "juan", "maria", "jose", "francia", "helena", "teresa", "jorge"]

#Metodo para mostrar el menú para elegir la carpeta donde se desea crear los archivos
def sacarFileChooser():
    carpeta=filedialog.askdirectory()
    rutaText.set(carpeta+"/")
    numArchivos.set(0)
    botonCrear.grid(column=3, row=2,columnspan=3)

#Método para mostrar el mensaje de éxito
def llamarConfirm():
    mensaje=tk.Message(ventanaPrincipal, text="Archivos creados con exito", font=("Helvetica",12))
    mensaje.grid(column=1,row=3,columnspan=3)

#Método para crear los 100 archivos junto a los 5 nombres escogidos al azar
def crearElementos():
    ruta = rutaText.get()
    for i in range(100):
        archivo = open(ruta +str(numArchivos.get())+ str(i) + ".txt", "w+")
        for i in range(5):
            nombre = random.randint(0, 9)
            archivo.write(nombres[nombre] + "\n")
        archivo.close()
    numArchivos.set(numArchivos.get()+1)
    llamarConfirm()

######Interfaz Gráfica###########
ventanaPrincipal= tk.Tk(className="Crear 100 archivos") #Ventana principal
rutaText=tk.StringVar() #Variable global para guardar la ruta
numArchivos=tk.IntVar() #Variable global para llevar registro de cuantas veces se ha realizado
ruta=tk.Label(ventanaPrincipal, text="Elegir carpeta: ", font=("Helvetica",12)).grid(column=1, row=1, columnspan=1) #Etiqueta
entrada=tk.Entry(ventanaPrincipal, textvariable=rutaText,font=("Helvetica",12)).grid(column=0, row=2, columnspan=3) #Campo de texto donde se muestra la ruta
botonBuscar = tk.Button(ventanaPrincipal, text="Buscar", command=sacarFileChooser, borderwidth=1, font=("Helvetica",12)).grid(row=1, column=3)
botonCrear=tk.Button(ventanaPrincipal, text="Crear", command=crearElementos, font=("Helvetica",12))
ventanaPrincipal.mainloop() #muestra la ventana








