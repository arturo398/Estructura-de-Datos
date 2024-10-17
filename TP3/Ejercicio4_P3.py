'''
En un cine, se dispone de 70 butacas distribuidas en 7 filas con 10 columnas cada una. El
objetivo es desarrollar un sistema de turnero que permita visualizar un mapa interactivo de
las butacas, mostrando cuáles están vacías y cuáles han sido reservadas .
Al momento de reservar un asiento , el sistema debe registrar el nombre y el teléfono del
cliente, y marcar el asiento como ocupado o reservado en el mapa. Además, se debe
proporcionar la funcionalidad de consultar la información del cliente que ha reservado un
lugar específico, permitiéndole ver sus datos de contacto .
'''
import tkinter as tk 
from tkinter import messagebox, simpledialog
#Crear ventana principal
root=tk.Tk()
root.title("Reserva de Butacas - Cine")


#Configuracion de los asientos 
f=6
c=6
asiento=[[0 for _ in range(c)] for _ in range(f)]
reservas={}

def reservar_butaca(fila, columna, boton):
    numero_asiento=fila*c+columna+1

    if asiento[fila][columna]==0:
        #Pedir datos del cliente
        nombre=simpledialog.askstring("Nombre", "Ingrese su nombre: " )
        telefono=simpledialog.askstring("Telefono", "Ingrese su numero de telefono: ")

        if nombre and telefono: #Comprobacion si se ingreso los datos
            asiento[fila][columna]=1
            reservas[numero_asiento]={"nombre":nombre, "telefono":telefono}
            boton.config(bg="red", text="Reservado")
            messagebox.showinfo("Reserva", f"Asiento {numero_asiento} reservado por {nombre}.")
        else: 
            messagebox.showinfo("Error", "Debe ingresar todos los datos")

    else:
        #Mostramos los datos de la reserva
        cliente=reservas.get(numero_asiento)
        if cliente :
            messagebox.showinfo("Informacion de reserva", f"Asiento {numero_asiento} esta reservado por {cliente['nombre']} \n Telefono: {cliente['telefono']}" )
        else:
            messagebox.showinfo("Error", "No se encontraron datos para este asiento")


#Crear botones para los asientos 
for i in range(f):
    for j in range(c):
        boton = tk.Button(root, text=f"Asiento \n {i*c+j+1}", width=10, height=3)  
        boton.config(command=lambda i=i, j=j, b=boton: reservar_butaca(i, j, b))
        boton.grid(row=i, column=j, padx=5, pady=5)

root.mainloop()