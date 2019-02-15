import tkinter as tk
from tkinter import filedialog

#Método para cargar el archivo y mostrar el nombre
def escogerArchivo():
    archivoACargar=filedialog.askopenfile(title="Elige el archivo",filetypes=(("fasta normal",".fa"),("fasta",".fasta"),("mfasta",".mpfa"),("nfasta",".fna"),("sfasta",".fas"),("fas",".fas"),("fasta",".fasta")))
    contar(archivoACargar)
    nombreArchivo=str(archivoACargar.name)
    nombreSplit=nombreArchivo.split("/")
    archivo.set(nombreSplit[nombreSplit.__len__()-1])

#Método que cuenta el total de cada aminoácido del archivo
def contar(archivoALeer):
    acidonucleicoT=0
    acidonucleicoA=0
    acidonucleicoC=0
    acidonucleicoG=0
    for lines in archivoALeer:
        if not lines.startswith('>'):
           acidonucleicoT+=lines.count("T")
           acidonucleicoC+= lines.count("C")
           acidonucleicoA+= lines.count("A")
           acidonucleicoG+= lines.count("G")
    crearDatos(acidonucleicoT,acidonucleicoA,acidonucleicoG,acidonucleicoC)

#Método que muestra en pantalla el total de aminoácidos, con su color corespondiente
def crearDatos(acidonucleicoT,acidonucleicoA,acidonucleicoG,acidonucleicoC):
    etiquetaT = tk.Label(ventanaPrincipal, text="Total aminoacidos T: " + str(acidonucleicoT), foreground="red",font=("Helvetica",12)).grid(column=2, row=1)
    etiquetaA = tk.Label(ventanaPrincipal, text="Total aminoacidos A: " + str(acidonucleicoA), foreground="orange",font=("Helvetica",12)).grid(column=2, row=2)
    etiquetaC = tk.Label(ventanaPrincipal, text="Total aminoacidos C: " + str(acidonucleicoC), foreground="blue",font=("Helvetica",12)).grid(column=2, row=3)
    etiquetaG = tk.Label(ventanaPrincipal, text="Total aminoacidos G: " + str(acidonucleicoG), foreground="green",font=("Helvetica",12)).grid(column=2, row=4)


####INTERFAZ GRÁFICA#####
ventanaPrincipal=tk.Tk(className="Conteo Acidosnucleicos")
botonCargar=tk.Button(ventanaPrincipal, text="Cargar Archivo", command=escogerArchivo,font=("Helvetica",12)).grid(column=1, row=1)
archivo=tk.StringVar()
archivoEscogido=tk.Entry(ventanaPrincipal, textvariable=archivo, font=("Helvetica",12)).grid(column=1, row=2)
ventanaPrincipal.mainloop()