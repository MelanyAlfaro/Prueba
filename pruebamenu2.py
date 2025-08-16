import tkinter as tk
from tkinter import ttk

DATA = {
    "Reportes": "Genera y exporta reportes en PDF/CSV.",
    "Estadísticas": "Panel de KPIs y gráficos.",
    "Proyectos": "Crea, edita y archiva proyectos.",
    "Usuarios": "Alta/baja y roles.",
    "Ajustes": "Preferencias del sistema.",
    "Ayuda": "FAQ y contacto.",
}

def show_detail(event=None):
    sel = lb.curselection()
    if not sel: return
    name = lb.get(sel[0])
    desc_var.set(DATA[name])

def open_selected():
    sel = lb.curselection()
    if not sel: return
    print("Abrir:", lb.get(sel[0]))

root = tk.Tk()
root.title("Menú")
root.geometry("720x420")
style = ttk.Style()
try: style.theme_use("clam")
except: pass

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=1)

left = ttk.Frame(root, padding=16); left.grid(row=0, column=0, sticky="nsew")
right = ttk.Frame(root, padding=16); right.grid(row=0, column=1, sticky="nsew")

ttk.Label(left, text="Opciones", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,8))
lb = tk.Listbox(left, activestyle="none", exportselection=False)
for k in DATA: lb.insert("end", k)
lb.pack(fill="both", expand=True)
lb.bind("<<ListboxSelect>>", show_detail)

desc_var = tk.StringVar(value="Selecciona una opción…")
ttk.Label(right, textvariable=desc_var, wraplength=420, justify="left").pack(fill="x")
ttk.Button(right, text="Abrir", command=open_selected).pack(anchor="e", pady=12)

lb.selection_set(0); show_detail()
root.mainloop()
