from tkinter import font
import tkinter as tk

#Método que captura la tecla pulsada en el teclado y realiza la acción correspondiente
def calcular(evento):
    if(evento.keysym=='1'):
        frameResultados.grid(column=2, row=0)
        interfazSumar("Sumar      ")
    elif(evento.keysym=='2'):
        frameResultados.grid(column=2, row=0)
        interfazRestar("Restar     ")
    elif(evento.keysym=='3'):
        frameResultados.grid(column=2, row=0)
        interfazMultiplicar("Multiplicar")
    elif(evento.keysym=='4'):
        frameResultados.grid(column=2, row=0)
        interfazDividir("Dividir    ")
    elif (evento.keysym == '5'):
        frameResultados.grid(column=2, row=0)
        interfazModulo("Modulo     ")
    elif(evento.keysym=='9'):
        salir()

#Método para generar la interfaz gráfica de cada operación
def realizarInterfaz(operacion):
    etiquetaTexto = tk.Label(frameResultados, text=operacion+" 2 números" , font=("Helvetica",12))
    etiquetaTexto.grid(column=0, row=1, columnspan=2)

    etiquetaNumero1 = tk.Label(frameResultados, text="Ingrese primer número:", font=("Helvetica",12))
    etiquetaNumero1.grid(column=0, row=2)
    etiquetaNumero2 = tk.Label(frameResultados, text="Ingrese segundo número:" , font=("Helvetica",12))
    etiquetaNumero2.grid(column=0, row=3)

    entrada1 = tk.Entry(frameResultados, textvariable=numero1 , font=("Helvetica",12))
    entrada1.grid(column=1, row=2)
    entrada2 = tk.Entry(frameResultados, textvariable=numero2 , font=("Helvetica",12))
    entrada2.grid(column=1, row=3)

    botonLimpiar = tk.Button(frameResultados, text="Limpiar", command=limpiarInterfaz , font=("Helvetica",12))
    botonLimpiar.grid(column=1, row=4, columnspan=2)

    frameResultados.focus_set()

#Método para limpiar los datos y volver al menú
def limpiarInterfaz():
    numero1.set(0)
    numero2.set(0)
    resultadoOperacion.set("")
    frameResultados.grid_remove()
    frameMenu.focus_set()

#Método que generá la interfaz de la suma, con el boton asociado
def interfazSumar(operacion):
    realizarInterfaz(operacion)
    botonCalcular = tk.Button(frameResultados, text=operacion, command=realizarSuma , font=("Helvetica",12))
    botonCalcular.grid(column=0, row=4, columnspan=2)

#Método que realiza la operacion matematica definida
def realizarSuma():
    try:
        int(numero1.get())
        int(numero2.get())
        resultadoOperacion.set(""+str(numero1.get()+numero2.get()))
    except tk.TclError:
        resultadoOperacion.set("Ingrese solo números")

    resultado = tk.Entry(frameResultados, textvariable=resultadoOperacion,font=("Helvetica",12))
    resultado.grid(column=0, row=5, columnspan=2)

def interfazRestar(operacion):
    realizarInterfaz(operacion)
    botonCalcular = tk.Button(frameResultados, text=operacion, command=realizarResta , font=("Helvetica",12))
    botonCalcular.grid(column=0, row=4, columnspan=2)

def realizarResta():
    try:
        int(numero1.get())
        int(numero2.get())
        resultadoOperacion.set("" + str(numero1.get() - numero2.get()))
    except tk.TclError:
        resultadoOperacion.set("Ingrese solo números")

    resultado = tk.Entry(frameResultados, textvariable=resultadoOperacion,font=("Helvetica",12))
    resultado.grid(column=0, row=5, columnspan=2)

def interfazMultiplicar(operacion):
    realizarInterfaz(operacion)
    botonCalcular = tk.Button(frameResultados, text=operacion, command=realizarMultiplicar , font=("Helvetica",12))
    botonCalcular.grid(column=0, row=4, columnspan=2)

def realizarMultiplicar():
    try:
        int(numero1.get())
        int(numero2.get())
        resultadoOperacion.set("" + str(numero1.get() * numero2.get()))
    except tk.TclError:
        resultadoOperacion.set("Ingrese solo números")

    resultado = tk.Entry(frameResultados, textvariable=resultadoOperacion,font=("Helvetica",12))
    resultado.grid(column=0, row=5, columnspan=2)

def interfazDividir(operacion):
    realizarInterfaz(operacion)
    botonCalcular = tk.Button(frameResultados, text=operacion, command=realizarDividir , font=("Helvetica",12))
    botonCalcular.grid(column=0, row=4, columnspan=2)

def realizarDividir():
    try:
        int(numero1.get())
        int(numero2.get())
        if not(numero2.get() ==0):
            resultadoOperacion.set("" + str(numero1.get() / numero2.get()))

        else:
            resultadoOperacion.set("División por 0 no permitida")
    except tk.TclError:
        resultadoOperacion.set("Ingrese solo números")

    resultado = tk.Entry(frameResultados, textvariable=resultadoOperacion,font=("Helvetica",12))
    resultado.grid(column=0, row=5, columnspan=2)


def interfazModulo(operacion):
    realizarInterfaz(operacion)
    botonCalcular = tk.Button(frameResultados, text=operacion, command=realizarModulo , font=("Helvetica",12))
    botonCalcular.grid(column=0, row=4, columnspan=2)

def realizarModulo():
    try:
        int(numero1.get())
        int(numero2.get())
        if not (numero2.get() == 0):
            resultadoOperacion.set("" + str(numero1.get() % numero2.get()))

        else:
            resultadoOperacion.set("División por 0 no permitida")
    except tk.TclError:
        resultadoOperacion.set("Ingrese solo números")

    resultado = tk.Entry(frameResultados, textvariable=resultadoOperacion,font=("Helvetica",12))
    resultado.grid(column=0, row=5, columnspan=2)

def salir():
    ventanaPrincipal.destroy()


#################INTERFAZ GRÁFICA####################
ventanaPrincipal=tk.Tk(className="Calculadora" )
numero1 = tk.IntVar()
numero2 = tk.IntVar()

frameMenu=tk.Frame(ventanaPrincipal,bd=3,height=50,width=50)
frameMenu.grid(column=0,row=0)
frameMenu.focus_set()
frameMenu.bind('<Key>',calcular)
titulo=tk.Label(frameMenu,text="-------------Calculadora en Python--------------", font=("Helvetica",12)).grid(column=0,row=0)
suma=tk.Label(frameMenu,text="1=Suma" , font=("Helvetica",12)).grid(column=0,row=1,columnspan=1,sticky="w")
resta=tk.Label(frameMenu,text="2=Resta" , font=("Helvetica",12)).grid(column=0,row=2,sticky="w")
multiplicacion=tk.Label(frameMenu,text="3=Multiplicación" , font=("Helvetica",12)).grid(column=0,row=3,sticky="w")
division=tk.Label(frameMenu,text="4=Division" , font=("Helvetica",12)).grid(column=0,row=4,sticky="w")
modulo=tk.Label(frameMenu,text="5=Módulo" , font=("Helvetica",12)).grid(column=0,row=5,sticky="w")
salirPrograma=tk.Label(frameMenu,text="9=Salir" , font=("Helvetica",12)).grid(column=0,row=6,sticky="w")

resultadoOperacion=tk.StringVar()
frameResultados=tk.Frame(ventanaPrincipal,bd=3,height=50,width=50)

ventanaPrincipal.focus_set()
ventanaPrincipal.mainloop()