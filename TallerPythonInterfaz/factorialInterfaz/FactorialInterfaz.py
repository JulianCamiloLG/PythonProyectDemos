import tkinter as tk

#Método que captura el valor ingresado y muestra en pantalla el resultado
def factorial():
    texto = tk.StringVar()
    try:
        int(numeroIngresado.get())
        valorIngresado=numeroIngresado.get()
        resultado=factorialRecursivo(valorIngresado)
        texto.set("Factorial: "+str(resultado))

    except tk.TclError:
        texto = tk.StringVar()
        texto.set("Ingrese un numero valido")

    label = tk.Entry(ventanaPrincipal,textvariable=texto, font=("Helvetica",12))
    label.grid(column=2, row=4, columnspan=2)



#Método que calcula el factorial de el valor ingresado de manera recursiva
def factorialRecursivo(valor):
    if(valor < 2):
        return 1
    else:
        return valor*factorialRecursivo(valor-1)

#Método para calcular el factorial pulsando la tecla enter en el campo de texto
def factorialEvento(evento):
    factorial()


####INTERFAZ GRÁFICA#####
ventanaPrincipal=tk.Tk(className="Factorial")
numeroIngresado=tk.IntVar()
etiquetaNumero=tk.Label(ventanaPrincipal,text="Ingrese el numero:", font=("Helvetica",12)).grid(column=2, row=1)
entradaNumero=tk.Entry(ventanaPrincipal,textvariable=numeroIngresado, font=("Helvetica",12))
entradaNumero.grid(column=3,row=1)
botonCalcular=tk.Button(ventanaPrincipal,text="Calcular", command=factorial, font=("Helvetica",12)).grid(column=2,row=3,columnspan=2)
entradaNumero.bind('<Return>',factorialEvento)
ventanaPrincipal.mainloop()
