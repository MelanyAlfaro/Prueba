import tkinter as tk
from tkinter import ttk

OPTIONS = [
    ("📄 Reportes", "Abrir módulo de reportes"),
    ("📊 Estadísticas", "Ver panel de métricas"),
    ("🗂️ Proyectos", "Gestionar proyectos"),
    ("👥 Usuarios", "Administrar usuarios"),
    ("⚙️ Ajustes", "Configuración general"),
    ("❓ Ayuda", "Documentación y soporte"),
]

def on_select(name):
    print(f"Abrir: {name}")  # aquí llamas tu lógica

root = tk.Tk()
root.title("Menú principal")
root.geometry("720x480")

# --- Estilo ---
style = ttk.Style()
try:
    style.theme_use("clam")
except tk.TclError:
    pass

style.configure("Tile.TButton",
                font=("Segoe UI", 12, "bold"),
                padding=14)
style.map("Tile.TButton",
          relief=[("active", "groove")])

# Marco principal con padding
container = ttk.Frame(root, padding=20)
container.pack(fill="both", expand=True)

# Hacer grid responsive
for r in range(3):
    container.rowconfigure(r, weight=1, uniform="r")
for c in range(2):
    container.columnconfigure(c, weight=1, uniform="c")

# Crear botones como “tiles”
for i, (title, subtitle) in enumerate(OPTIONS):
    r, c = divmod(i, 2)
    card = ttk.Frame(container, padding=16, style="Card.TFrame")
    card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
    card.columnconfigure(0, weight=1)

    # Título grande (usa emoji como icono)
    lbl_title = ttk.Label(card, text=title, font=("Segoe UI", 14, "bold"))
    lbl_title.grid(row=0, column=0, sticky="w")

    # Subtítulo
    lbl_sub = ttk.Label(card, text=subtitle, foreground="#555")
    lbl_sub.grid(row=1, column=0, sticky="w", pady=(6, 12))

    # Botón de acción
    btn = ttk.Button(card, text="Abrir", style="Tile.TButton",
                     command=lambda n=title: on_select(n))
    btn.grid(row=2, column=0, sticky="ew")

    # Hover visual en el frame (cambia fondo sutil)
    def enter(e, f=card): f.configure(style="CardHover.TFrame")
    def leave(e, f=card): f.configure(style="Card.TFrame")
    card.bind("<Enter>", enter)
    card.bind("<Leave>", leave)

# Estilos para “cards”
style.configure("Card.TFrame", relief="ridge", borderwidth=1)
style.configure("CardHover.TFrame", relief="solid", borderwidth=2)

# Atajos de teclado Alt+1…Alt+6
for idx, (title, _) in enumerate(OPTIONS, start=1):
    root.bind_all(f"<Alt-KeyPress-{idx}>", lambda e, n=title: on_select(n))

root.mainloop()
