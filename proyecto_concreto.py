import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("calculadora de mezclas de concreto")
ventana.geometry("1050x500")

# Diseño de la mezcla

# Paso 1: Calcular el asentamiento

# Lista de opciones
opciones = ["Seleccionar","Asentamiento", "Consistencia de la mezcla", "Tipo de construcción, sistema de colocación y el sistema de compactación"]

# Crear el combobox de pregunta
pregunta_asentamiento = tk.Label(ventana, text="¿Que datos conoce de la mezcla?")
pregunta_asentamiento.pack(pady=5)
combo = ttk.Combobox(ventana, values=opciones)
combo.current(0)  # Selecciona la primera opción por defecto
combo.pack(pady=10)

# Combobox 1: Tipo de construcción
label1 = tk.Label(ventana, text="Tipo de construcción")
label1.pack(pady=5)
combo1 = ttk.Combobox(ventana, values=list(tabla_asentamiento.keys()), width=80, state="readonly")
combo1.pack(pady=5)

# Combobox 2: Sistema de colocación
label2 = tk.Label(ventana, text="Sistema de colocación")
label2.pack(pady=5)
combo2 = ttk.Combobox(ventana, width=80, state="readonly")
combo2.pack(pady=5)

# Combobox 3: Sistema de compactación
label3 = tk.Label(ventana, text="Sistema de compactación")
label3.pack(pady=5)
combo3 = ttk.Combobox(ventana, width=80, state="readonly")
combo3.pack(pady=5)

# Etiqueta de resultado
etiqueta = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta.pack(pady=10)

def actualizar_colocacion(event):
    seleccion_construccion = combo1.get()
    if seleccion_construccion in tabla_asentamiento:
        opciones_colocacion = list(tabla_asentamiento[seleccion_construccion].keys())
        combo2["values"] = opciones_colocacion
        combo2.set("")  # limpiar selección previa
        combo3.set("")  # limpiar compactación
        etiqueta.config(text="")  # limpiar resultado

# Función para mostrar la opción seleccionada
def mostrar_seleccion():
    seleccion = combo.get()
    etiqueta.config(text=f"Seleccionaste: {seleccion}")

# Botón para confirmar selección
boton_calcular = tk.Button(ventana, text="Calcular asentamiento", command=calcular_asentamiento)
boton_calcular.pack(pady=10)

# Diccionario con las combinaciones de datos y su asentamiento
tabla_asentamiento = {
    ("Prefabricados de alta resistencia; revestimiento de pantallas de cimentación",
     "Con vibradores de formaleta; concretos de proyección neumática (lanzado)",
     "Secciones con vibradores de vibración extrema, puede requerirse"): "0-20 mm",

    ("Pavimentos",
     "Pavimentadoras con terminadora vibratoria",
     "Secciones sujetas a vibración"): "20-35 mm",

    ("Pavimentos, fundaciones en concreto simple",
     "Colocación con máquinas o empleados manualmente",
     "Secciones simplemente reforzadas, con vibración"): "35-50 mm",

    ("Pavimentos compactados a mano, losas macizas, vigas",
     "Colocación manual",
     "Secciones medianamente reforzadas, sin vibración"): "50-100 mm",

    ("Elementos estructurales esbeltos",
     "Bombeo",
     "Secciones bastante reforzadas, sin vibración"): "100-150 mm",

    ("Elementos muy esbeltos, fundidos in situ",
     "Tubo-embudo Tremie",
     "Secciones altamente reforzadas, sin vibradores (Normalmente no adecuados para vibrarse)"): "150 mm o más"
}


ventana.mainloop()
# sexo