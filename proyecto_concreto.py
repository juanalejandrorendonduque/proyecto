import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("calculadora de mezclas de concreto")
ventana.geometry("1050x500")

# Lista de opciones
opciones = ["Seleccionar","Asentamiento", "Consistencia de la mezcla", "Tipo de construcción, sistema de colocación y el sistema de compactación"]

# Crear el combobox
pregunta_asentamiento = tk.Label(ventana, text="¿Que datos conoce de la mezcla?")
pregunta_asentamiento.pack(pady=5)
combo = ttk.Combobox(ventana, values=opciones)
combo.current(0)  # Selecciona la primera opción por defecto
combo.pack(pady=10)

# Función para mostrar la opción seleccionada
def mostrar_seleccion():
    seleccion = combo.get()
    etiqueta.config(text=f"Seleccionaste: {seleccion}")

# Botón para confirmar selección
boton = tk.Button(ventana, text="Confirmar", command=mostrar_seleccion)
boton.pack(pady=5)

# Etiqueta para mostrar resultado
etiqueta = tk.Label(ventana, text="")
etiqueta.pack(pady=5)

ventana.mainloop()
