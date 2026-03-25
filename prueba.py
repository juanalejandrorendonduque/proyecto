import tkinter as tk
from tkinter import ttk

# ─────────────────────────────────────────────
#  DATOS DE LA TABLA (cada fila es un dict)
# ─────────────────────────────────────────────
DATOS_CONCRETO = {
    "Prefabricados de alta resistencia / Revestimiento de pantallas": {
        "consistencia": "Muy seca",
        "asentamiento": "0 – 20 mm",
        "sistema_colocacion": "Con vibradores de formaleta; concretos de proyección neumática (lanzado)",
        "sistema_compactacion": "Secciones sujetas a vibración extrema, puede seguirse presión",
    },
    "Pavimentos (mezcla seca)": {
        "consistencia": "Seca",
        "asentamiento": "20 – 35 mm",
        "sistema_colocacion": "Pavimentadoras con terminadora vibratoria",
        "sistema_compactacion": "Secciones sujetas a vibración intensa",
    },
    "Pavimentos / Fundaciones en concreto simple": {
        "consistencia": "Semi-seca",
        "asentamiento": "35 – 50 mm",
        "sistema_colocacion": "Colocación con máquinas operadas manualmente",
        "sistema_compactacion": "Secciones simplemente reforzadas, con vibración",
    },
    "Pavimentos compactados a mano / Losas / Muros / Vigas": {
        "consistencia": "Media",
        "asentamiento": "50 – 100 mm",
        "sistema_colocacion": "Colocación manual",
        "sistema_compactacion": "Secciones medianamente reforzadas, sin vibración",
    },
    "Elementos estructurales esbeltos": {
        "consistencia": "Húmeda",
        "asentamiento": "100 – 150 mm",
        "sistema_colocacion": "Bombeo",
        "sistema_compactacion": "Secciones bastante reforzadas, sin vibración",
    },
    "Elementos muy esbeltos / Pilotes fundidos in situ": {
        "consistencia": "Muy húmeda",
        "asentamiento": "150 mm o más",
        "sistema_colocacion": "Tubo-embudo Tremie",
        "sistema_compactacion": "Secciones altamente reforzadas, sin vibración (normalmente no adecuadas para vibrarse)",
    },
}

# ─────────────────────────────────────────────
#  COLORES Y ESTILOS
# ─────────────────────────────────────────────
BG_DARK   = "#1e1e2e"
BG_CARD   = "#2a2a3e"
BG_FIELD  = "#313145"
ACCENT    = "#7c6af7"
ACCENT2   = "#a78bfa"
TEXT_MAIN = "#e2e2f0"
TEXT_SUB  = "#9898b8"
TEXT_VAL  = "#ffffff"
BORDER    = "#3d3d5c"

FONT_TITLE   = ("Segoe UI", 20, "bold")
FONT_SUBTITLE= ("Segoe UI", 10)
FONT_LABEL   = ("Segoe UI", 9, "bold")
FONT_VALUE   = ("Segoe UI", 10)
FONT_COMBO   = ("Segoe UI", 10)
FONT_BTN     = ("Segoe UI", 11, "bold")
FONT_SCREEN  = ("Segoe UI", 16, "bold")


# ─────────────────────────────────────────────
#  PANTALLA DE INICIO
# ─────────────────────────────────────────────
class PantallaInicio(tk.Frame):
    def __init__(self, parent, on_crear_mezcla):
        super().__init__(parent, bg=BG_DARK)
        self._on_crear_mezcla = on_crear_mezcla
        self._build()

    def _build(self):
        tk.Frame(self, bg=BG_DARK, height=80).pack()

        tk.Label(
            self, text="🏗",
            font=("Segoe UI", 52), bg=BG_DARK
        ).pack()

        tk.Frame(self, bg=BG_DARK, height=16).pack()

        tk.Label(
            self,
            text="Generación de Mezclas\nde Concreto",
            font=FONT_TITLE, bg=BG_DARK, fg=TEXT_VAL,
            justify="center"
        ).pack()

        tk.Frame(self, bg=BG_DARK, height=10).pack()

        tk.Label(
            self,
            text="Selecciona el tipo de construcción para obtener\nel sistema de colocación y compactación recomendado.",
            font=FONT_SUBTITLE, bg=BG_DARK, fg=TEXT_SUB,
            justify="center"
        ).pack()

        tk.Frame(self, bg=BG_DARK, height=48).pack()

        tk.Frame(self, bg=BORDER, width=260, height=1).pack()

        tk.Frame(self, bg=BG_DARK, height=48).pack()

        btn = tk.Button(
            self,
            text="  ➕  Crear Mezcla de Concreto",
            font=FONT_BTN,
            bg=ACCENT,
            fg=TEXT_VAL,
            activebackground=ACCENT2,
            activeforeground=TEXT_VAL,
            relief="flat",
            bd=0,
            padx=28,
            pady=14,
            cursor="hand2",
            command=self._on_crear_mezcla,
        )
        btn.pack()

        btn.bind("<Enter>", lambda e: btn.config(bg=ACCENT2))
        btn.bind("<Leave>", lambda e: btn.config(bg=ACCENT))


# ─────────────────────────────────────────────
#  PANTALLA SELECTOR DE MEZCLA
# ─────────────────────────────────────────────
class PantallaSelector(tk.Frame):
    def __init__(self, parent, on_volver, app_ref):
        super().__init__(parent, bg=BG_DARK)
        self._on_volver = on_volver
        self._app = app_ref
        self._build()

    def _build(self):
        # Barra superior
        top_bar = tk.Frame(self, bg=BG_DARK)
        top_bar.pack(fill="x", padx=20, pady=(14, 0))

        btn_volver = tk.Button(
            top_bar,
            text="← Volver",
            font=("Segoe UI", 9),
            bg=BG_FIELD, fg=TEXT_SUB,
            activebackground=BORDER, activeforeground=TEXT_VAL,
            relief="flat", bd=0, padx=10, pady=5,
            cursor="hand2",
            command=self._on_volver,
        )
        btn_volver.pack(side="left")

        tk.Label(
            self, text="🏗  Clasificación de Concreto",
            font=FONT_SCREEN, bg=BG_DARK, fg=ACCENT2
        ).pack(pady=(16, 4))

        tk.Label(
            self,
            text="Selecciona el tipo de construcción para ver los sistemas recomendados",
            font=("Segoe UI", 9), bg=BG_DARK, fg=TEXT_SUB
        ).pack(pady=(0, 18))

        # Dropdown
        frame_sel = tk.Frame(self, bg=BG_DARK)
        frame_sel.pack(padx=40, fill="x")

        tk.Label(
            frame_sel, text="Tipo de construcción",
            font=FONT_LABEL, bg=BG_DARK, fg=TEXT_SUB
        ).pack(anchor="w", pady=(0, 4))

        style = ttk.Style()
        style.configure(
            "Custom.TCombobox",
            fieldbackground=BG_FIELD,
            background=BG_FIELD,
            foreground=TEXT_VAL,
            arrowcolor=ACCENT2,
            bordercolor=BORDER,
            lightcolor=BORDER,
            darkcolor=BORDER,
            padding=8,
            font=FONT_COMBO,
        )
        style.map("Custom.TCombobox",
                  fieldbackground=[("readonly", BG_FIELD)],
                  foreground=[("readonly", TEXT_VAL)])

        self.selected = tk.StringVar()
        opciones = list(DATOS_CONCRETO.keys())
        self.combo = ttk.Combobox(
            frame_sel,
            textvariable=self.selected,
            values=opciones,
            state="readonly",
            style="Custom.TCombobox",
            width=70,
        )
        self.combo.pack(fill="x")
        self.combo.bind("<<ComboboxSelected>>", self._on_select)

        # Tarjeta de resultados
        self.card = tk.Frame(self, bg=BG_CARD, bd=0, relief="flat")
        self.card.pack(padx=40, pady=24, fill="both", expand=True)

        self.placeholder = tk.Label(
            self.card,
            text="⬆  Selecciona un tipo de construcción\npara ver los sistemas recomendados",
            font=("Segoe UI", 11), bg=BG_CARD, fg=TEXT_SUB,
            justify="center"
        )
        self.placeholder.pack(expand=True)

        self.fields_frame = tk.Frame(self.card, bg=BG_CARD)

        self._make_field(self.fields_frame, "📐  Consistencia",           "val_consistencia")
        self._separator(self.fields_frame)
        self._make_field(self.fields_frame, "📏  Asentamiento",           "val_asentamiento")
        self._separator(self.fields_frame)
        self._make_field(self.fields_frame, "🚜  Sistema de colocación",  "val_colocacion")
        self._separator(self.fields_frame)
        self._make_field(self.fields_frame, "🔧  Sistema de compactación","val_compactacion")

    def _make_field(self, parent, label_text, val_attr):
        row = tk.Frame(parent, bg=BG_CARD, pady=10, padx=20)
        row.pack(fill="x")
        tk.Label(
            row, text=label_text,
            font=FONT_LABEL, bg=BG_CARD, fg=TEXT_SUB, anchor="w"
        ).pack(fill="x")
        val_lbl = tk.Label(
            row, text="—",
            font=FONT_VALUE, bg=BG_CARD, fg=TEXT_VAL,
            anchor="w", wraplength=580, justify="left"
        )
        val_lbl.pack(fill="x", pady=(2, 0))
        setattr(self, val_attr, val_lbl)

    def _separator(self, parent):
        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x", padx=20)

    def _on_select(self, _event=None):
        key = self.selected.get()
        if not key:
            return

        datos = DATOS_CONCRETO[key]

        # Guardar en variables individuales de la app
        self._app.tipo_construccion    = key
        self._app.consistencia         = datos["consistencia"]
        self._app.asentamiento         = datos["asentamiento"]
        self._app.sistema_colocacion   = datos["sistema_colocacion"]
        self._app.sistema_compactacion = datos["sistema_compactacion"]

        # Ocultar placeholder y mostrar campos
        self.placeholder.pack_forget()
        self.fields_frame.pack(fill="both", expand=True, pady=10)

        # Actualizar UI
        self.val_consistencia.config(text=self._app.consistencia)
        self.val_asentamiento.config(text=self._app.asentamiento)
        self.val_colocacion.config(text=self._app.sistema_colocacion)
        self.val_compactacion.config(text=self._app.sistema_compactacion)


# ─────────────────────────────────────────────
#  APLICACIÓN PRINCIPAL
# ─────────────────────────────────────────────
class ConcreteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Generación de Mezclas de Concreto")
        self.configure(bg=BG_DARK)
        self.resizable(False, False)

        # Variables de selección
        self.tipo_construccion    = None
        self.consistencia         = None
        self.asentamiento         = None
        self.sistema_colocacion   = None
        self.sistema_compactacion = None

        # Estilos globales
        style = ttk.Style(self)
        style.theme_use("clam")

        # Centrar ventana
        w, h = 680, 620
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

        # Contenedor de pantallas
        self.container = tk.Frame(self, bg=BG_DARK)
        self.container.pack(fill="both", expand=True)

        self.pantalla_inicio   = PantallaInicio(self.container, on_crear_mezcla=self._ir_a_selector)
        self.pantalla_selector = PantallaSelector(self.container, on_volver=self._ir_a_inicio, app_ref=self)

        # Arrancar en la pantalla de inicio
        self._mostrar(self.pantalla_inicio)

    def _mostrar(self, pantalla):
        """Oculta todas las pantallas y muestra la indicada."""
        for frame in (self.pantalla_inicio, self.pantalla_selector):
            frame.place_forget()
        pantalla.place(relx=0, rely=0, relwidth=1, relheight=1)

    def _ir_a_selector(self):
        self._mostrar(self.pantalla_selector)

    def _ir_a_inicio(self):
        self._mostrar(self.pantalla_inicio)

    def get_seleccion(self):
        """Retorna un dict con todas las variables de la selección actual."""
        return {
            "tipo_construccion":    self.tipo_construccion,
            "consistencia":         self.consistencia,
            "asentamiento":         self.asentamiento,
            "sistema_colocacion":   self.sistema_colocacion,
            "sistema_compactacion": self.sistema_compactacion,
        }


if __name__ == "__main__":
    app = ConcreteApp()
    app.mainloop()