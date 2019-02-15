import tkinter as tk
from math import sqrt


#Método que toma los datos y los muestra en pantalla
def fibonacci():
    respuesta = tk.StringVar()
    try:
        int(valorIngresado.get())
        entrada=valorIngresado.get()
        serieFibo=fibonacciReducido(entrada)
        respuesta=tk.StringVar()
        respuesta.set("Fibonacci: "+str(serieFibo))

    except tk.TclError:

        respuesta.set("Ingrese solo números")

    label = tk.Entry(ventanaPrincipal, textvariable=respuesta,font=("Helvetica",12))
    label.grid(column=2, row=4, columnspan=2)

#Método que calcula el fibonacchi con la formula explícita, más rapida
def fibonacciReducido(entrada):
    fibonacciRespuesta= ((1 + sqrt(5)) ** entrada - (1 - sqrt(5)) ** entrada) / (2 ** entrada * sqrt(5))
    return round(fibonacciRespuesta,0)

def fibonacciRecursivoEjemplo():
    respuesta = tk.StringVar()
    try:
        int(valorIngresado.get())
        entrada = valorIngresado.get()
        serieFibo = fibonacciRecursivo(entrada)
        respuesta = tk.StringVar()
        respuesta.set("Fibonacci: " + str(serieFibo))

    except tk.TclError:

        respuesta.set("Ingrese solo números")

    label = tk.Entry(ventanaPrincipal, textvariable=respuesta, font=("Helvetica",12))
    label.grid(column=2, row=4, columnspan=2)

#Método que calcula el fibonacchi de manera recursiva, mucho más lenta
def fibonacciRecursivo(entrada):
    if(entrada==1):
        return 1
    elif(entrada==0):
        return 0
    else:
        return fibonacciRecursivo(entrada-2)+ fibonacciRecursivo(entrada-1)

def fiboEvento(evento):
    fibonacci()

####INTERFAZ GRÁFICA#####
ventanaPrincipal=tk.Tk(className="Factorial")
valorIngresado=tk.IntVar()
etiquetaNumero=tk.Label(ventanaPrincipal,text="Ingrese el numero:", font=("Helvetica",12)).grid(column=2, row=1)
entradaNumero=tk.Entry(ventanaPrincipal, textvariable=valorIngresado, font=("Helvetica",12))
entradaNumero.grid(column=3,row=1)
botonCalcular=tk.Button(ventanaPrincipal,text="Calcular", command=fibonacci, font=("Helvetica",12)).grid(column=2,row=3,columnspan=1)
botonCalcularRecursivo=tk.Button(ventanaPrincipal,text="Calcular Recursivo", command=fibonacciRecursivoEjemplo, font=("Helvetica",12)).grid(column=3,row=3,columnspan=1)
entradaNumero.bind('<Return>',fiboEvento)
ventanaPrincipal.mainloop()
