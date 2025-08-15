import tkinter as tk
from tkinter import ttk

# Datos ficticios
misiones_data = [
    {
        "usuario": "NeoTrek",
        "mision": "Reparar satélite",
        "objetivo": "Diagnóstico general",
        "recurso": "Terminal portátil",
        "fecha": "2025-08-04",
        "hora": "14:35",
        "resultado": "Completado",
        "notas": "Sin incidentes"
    },
    {
        "usuario": "StarGirl",
        "mision": "Monitorear estación",
        "objetivo": "Revisión sensores",
        "recurso": "Kit herramientas",
        "fecha": "2025-08-05",
        "hora": "09:20",
        "resultado": "Pendiente",
        "notas": "Esperando piezas"
    },
    {
        "usuario": "NeoTrek",
        "mision": "Monitorear estación",
        "objetivo": "Revisión sensores",
        "recurso": "Terminal portátil",
        "fecha": "2025-08-06",
        "hora": "10:15",
        "resultado": "Completado",
        "notas": "Todo en orden"
    }
]

def get_unique(field):
    return sorted(set(m[field] for m in misiones_data))

usuarios = get_unique("usuario")
misiones = get_unique("mision")
objetivos = get_unique("objetivo")
recursos = get_unique("recurso")

def actualizar_listas(event=None):
    selected_usuario = lista_usuario.get(tk.ANCHOR)
    selected_mision = lista_mision.get(tk.ANCHOR)
    selected_objetivo = lista_objetivo.get(tk.ANCHOR)
    selected_recurso = lista_recurso.get(tk.ANCHOR)

    # 🎯 Si selecciona NeoTrek, mostrar algo inventado de inmediato
    if selected_usuario == "NeoTrek":
        detalles_var.set("📡 NeoTrek reporta: \n\nTodo el sistema funcionando al 100%.\nÚltima misión completada sin incidentes.")
        return

    filtrado = misiones_data
    if selected_usuario:
        filtrado = [m for m in filtrado if m["usuario"] == selected_usuario]
    if selected_mision:
        filtrado = [m for m in filtrado if m["mision"] == selected_mision]
    if selected_objetivo:
        filtrado = [m for m in filtrado if m["objetivo"] == selected_objetivo]
    if selected_recurso:
        filtrado = [m for m in filtrado if m["recurso"] == selected_recurso]

    if not selected_usuario:
        lista_usuario.delete(0, tk.END)
        for u in sorted(set(m["usuario"] for m in filtrado)):
            lista_usuario.insert(tk.END, u)
    if not selected_mision:
        lista_mision.delete(0, tk.END)
        for mi in sorted(set(m["mision"] for m in filtrado)):
            lista_mision.insert(tk.END, mi)
    if not selected_objetivo:
        lista_objetivo.delete(0, tk.END)
        for o in sorted(set(m["objetivo"] for m in filtrado)):
            lista_objetivo.insert(tk.END, o)
    if not selected_recurso:
        lista_recurso.delete(0, tk.END)
        for r in sorted(set(m["recurso"] for m in filtrado)):
            lista_recurso.insert(tk.END, r)

    if selected_usuario and selected_mision and selected_objetivo and selected_recurso:
        for m in filtrado:
            detalles_var.set(
                f"Fecha: {m['fecha']}  Hora: {m['hora']}\n"
                f"Resultado: {m['resultado']}\n"
                f"Notas: {m['notas']}"
            )
            break

# Ventana principal
root = tk.Tk()
root.title("Filtro de Misiones - Ejemplo")
root.geometry("800x400")

# Tema y estilo
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", background="#e6f0ff", foreground="#003366", font=("Segoe UI", 10, "bold"))
style.configure("TFrame", background="#e6f0ff")
style.configure("Detalle.TLabel", background="#cce0ff", foreground="#003366", font=("Segoe UI", 11))

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure((0, 1, 2, 3), weight=1)
frame.rowconfigure(1, weight=1)

# Listas
lista_usuario = tk.Listbox(frame, exportselection=False)
lista_mision = tk.Listbox(frame, exportselection=False)
lista_objetivo = tk.Listbox(frame, exportselection=False)
lista_recurso = tk.Listbox(frame, exportselection=False)

for u in usuarios: lista_usuario.insert(tk.END, u)
for mi in misiones: lista_mision.insert(tk.END, mi)
for o in objetivos: lista_objetivo.insert(tk.END, o)
for r in recursos: lista_recurso.insert(tk.END, r)

# Etiquetas
ttk.Label(frame, text="Usuarios").grid(row=0, column=0, sticky="ew", pady=2)
ttk.Label(frame, text="Misiones").grid(row=0, column=1, sticky="ew", pady=2)
ttk.Label(frame, text="Objetivos").grid(row=0, column=2, sticky="ew", pady=2)
ttk.Label(frame, text="Recursos").grid(row=0, column=3, sticky="ew", pady=2)

lista_usuario.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
lista_mision.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
lista_objetivo.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
lista_recurso.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

# Eventos
for lista in (lista_usuario, lista_mision, lista_objetivo, lista_recurso):
    lista.bind("<<ListboxSelect>>", actualizar_listas)

# Detalles
detalles_var = tk.StringVar()
ttk.Label(frame, textvariable=detalles_var, style="Detalle.TLabel", padding=10).grid(
    row=2, column=0, columnspan=4, sticky="nsew", pady=10
)

root.mainloop()
