import tkinter as tk
from tkinter import ttk

# -----------------------
# Datos de ejemplo (simularán la salida de tu parser)
# -----------------------
data = [
    {"usuario": "NeoTrek", "mision": "Reconexión satélite", "objetivo": "Diagnóstico general",
     "recurso": "Terminal portátil", "fecha": "2025-08-04", "hora": "14:35",
     "resultado": "Completado", "notas": "Operación sin inconvenientes"},
    {"usuario": "AstroVega", "mision": "Exploración cavernas", "objetivo": "Mapeo 3D",
     "recurso": "Drone XR", "fecha": "2025-08-05", "hora": "09:15",
     "resultado": "Pendiente", "notas": "Esperando condiciones óptimas"},
    {"usuario": "NeoTrek", "mision": "Instalación sistema energético", "objetivo": "Calibración nodos",
     "recurso": "Kit herramientas", "fecha": "2025-08-06", "hora": "16:50",
     "resultado": "Completado", "notas": "Revisión final completada"},
    {"usuario": "LunaOps", "mision": "Reconexión satélite", "objetivo": "Reemplazo antena",
     "recurso": "Kit herramientas", "fecha": "2025-08-07", "hora": "11:20",
     "resultado": "Fallido", "notas": "Fallo durante despliegue"},
    {"usuario": "AstroVega", "mision": "Reconexión satélite", "objetivo": "Diagnóstico general",
     "recurso": "Terminal portátil", "fecha": "2025-08-08", "hora": None,
     "resultado": "Completado", "notas": "Sin hora registrada"},
]

# -----------------------
# Aplicación
# -----------------------
class MissionFilterApp:
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.root.title("Filtro de Misiones - OrbitOps")
        self.root.geometry("1000x560")
        self.root.configure(bg="#e6f4ff")

        # Style azul
        style = ttk.Style(self.root)
        style.theme_use('default')
        style.configure("TLabel", background="#e6f4ff", foreground="#013a63", font=("Segoe UI", 10))
        style.configure("Title.TLabel", font=("Segoe UI", 12, "bold"))
        style.configure("TButton", font=("Segoe UI", 10))
        style.configure("Treeview", font=("Segoe UI", 10), background="white")
        style.map("TButton", foreground=[('pressed', '#ffffff'), ('active', '#ffffff')])

        # Flag para evitar eventos recursivos mientras actualizamos controls
        self._updating = False

        # Variables de combobox (stringvars)
        self.user_var = tk.StringVar()
        self.mission_var = tk.StringVar()
        self.objective_var = tk.StringVar()
        self.resource_var = tk.StringVar()

        # Layout: filtros arriba, treeview abajo, detalle a la derecha
        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill="x", padx=12, pady=12)

        # Comboboxes: añadimos opción "Todos" para no filtrar
        self.cmb_user = self._make_combo(top_frame, "Usuario", self.user_var, 0)
        self.cmb_mission = self._make_combo(top_frame, "Misión", self.mission_var, 1)
        self.cmb_objective = self._make_combo(top_frame, "Objetivo", self.objective_var, 2)
        self.cmb_resource = self._make_combo(top_frame, "Recurso", self.resource_var, 3)

        # Reset button
        reset_btn = ttk.Button(top_frame, text="Limpiar filtros", command=self.reset_filters)
        reset_btn.grid(row=0, column=4, padx=10, sticky="w")

        # Middle: Treeview con coincidencias
        middle_frame = ttk.Frame(self.root)
        middle_frame.pack(fill="both", expand=True, padx=12, pady=(0,12))

        self.tree = ttk.Treeview(middle_frame, columns=("usuario","mision","objetivo","recurso","fecha"), show="headings", height=12)
        for col, text in [("usuario","Usuario"),("mision","Misión"),("objetivo","Objetivo"),("recurso","Recurso"),("fecha","Fecha")]:
            self.tree.heading(col, text=text)
            self.tree.column(col, width=160, anchor="w")
        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(middle_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="left", fill="y")

        # Panel derecho: detalles del registro seleccionado o mensaje
        right_panel = ttk.Frame(middle_frame, width=280)
        right_panel.pack(side="left", fill="y", padx=(12,0))

        ttk.Label(right_panel, text="Detalles / Resultado", style="Title.TLabel").pack(anchor="w", pady=(0,8))
        self.detail_text = tk.Text(right_panel, width=36, height=14, wrap="word", bg="#f7fbff", fg="#012a44", font=("Segoe UI", 10))
        self.detail_text.pack(pady=(0,8))
        self.detail_text.config(state="disabled")

        # Mensaje de estado
        self.status_label = ttk.Label(self.root, text="", font=("Segoe UI",10))
        self.status_label.pack(anchor="w", padx=14)

        # Bindings: detectar cambios (usamos trace para StringVar)
        self.user_var.trace_add("write", lambda *a: self.on_filter_change())
        self.mission_var.trace_add("write", lambda *a: self.on_filter_change())
        self.objective_var.trace_add("write", lambda *a: self.on_filter_change())
        self.resource_var.trace_add("write", lambda *a: self.on_filter_change())

        # También bind selección en treeview para mostrar detalles
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Inicializar valores
        self.reset_filters()

    def _make_combo(self, parent, label_text, var, col):
        ttk.Label(parent, text=label_text).grid(row=0, column=col*1, padx=(0,6), sticky="w")
        combo = ttk.Combobox(parent, textvariable=var, state="readonly", width=28)
        combo.grid(row=1, column=col*1, padx=(0,10), sticky="w")
        return combo

    def reset_filters(self):
        # Pone todo a "Todos"
        self._updating = True
        try:
            self.user_var.set("Todos")
            self.mission_var.set("Todos")
            self.objective_var.set("Todos")
            self.resource_var.set("Todos")
            # actualizar combobox values según datos completos
            self._set_combo_values(self.cmb_user, sorted({d["usuario"] for d in self.data}))
            self._set_combo_values(self.cmb_mission, sorted({d["mision"] for d in self.data}))
            self._set_combo_values(self.cmb_objective, sorted({d["objetivo"] for d in self.data}))
            self._set_combo_values(self.cmb_resource, sorted({d["recurso"] for d in self.data}))
        finally:
            self._updating = False
        self.update_results()

    def _set_combo_values(self, combo, items):
        # combo es ttk.Combobox; siempre ponemos "Todos" al inicio
        values = ["Todos"] + items
        combo['values'] = values
        # Si el valor actual no está en values, lo dejamos en "Todos"
        cur = combo.get()
        if cur not in values:
            combo.set("Todos")

    def on_filter_change(self):
        if self._updating:
            return
        self.update_results()

    def update_results(self):
        """
        Aplica el filtrado según comboboxes, repuebla comboboxes con
        solo los valores válidos para las otras dimensiones y actualiza el treeview.
        """
        self._updating = True
        try:
            # leer selecciones (si "Todos" -> no filtrar)
            u = self.user_var.get()
            m = self.mission_var.get()
            o = self.objective_var.get()
            r = self.resource_var.get()

            def matches(rec):
                if u != "Todos" and rec["usuario"] != u: return False
                if m != "Todos" and rec["mision"] != m: return False
                if o != "Todos" and rec["objetivo"] != o: return False
                if r != "Todos" and rec["recurso"] != r: return False
                return True

            filtered = [rec for rec in self.data if matches(rec)]

            # Repoblar comboboxes con valores coherentes según 'filtered'
            # Pero NO cambiar la selección actual si sigue siendo válida.
            possible_users = sorted({d["usuario"] for d in filtered}) if filtered else []
            possible_missions = sorted({d["mision"] for d in filtered}) if filtered else []
            possible_objectives = sorted({d["objetivo"] for d in filtered}) if filtered else []
            possible_resources = sorted({d["recurso"] for d in filtered}) if filtered else []

            # Si filtered está vacío, mostrar todas las opciones disponibles globalmente
            if not filtered:
                possible_users = sorted({d["usuario"] for d in self.data})
                possible_missions = sorted({d["mision"] for d in self.data})
                possible_objectives = sorted({d["objetivo"] for d in self.data})
                possible_resources = sorted({d["recurso"] for d in self.data})

            # Actualizar combobox values (sin seleccionar/des-seleccionar innecesariamente)
            self._set_combo_values(self.cmb_user, possible_users)
            self._set_combo_values(self.cmb_mission, possible_missions)
            self._set_combo_values(self.cmb_objective, possible_objectives)
            self._set_combo_values(self.cmb_resource, possible_resources)

            # Si la selección actual quedó fuera por ser incompatible, poner "Todos" (ya maneja _set_combo_values)
            # Actualizar treeview con 'filtered'
            for row in self.tree.get_children():
                self.tree.delete(row)
            for idx, rec in enumerate(filtered):
                fecha = rec.get("fecha", "")
                self.tree.insert("", "end", iid=str(idx), values=(rec["usuario"], rec["mision"], rec["objetivo"], rec["recurso"], fecha))

            # Estado: mostrar cuántas coincidencias hay
            self.status_label.config(text=f"Coincidencias: {len(filtered)} registros")

            # Si las 4 están seleccionadas (no "Todos") y hay exactamente 1 coincidencia -> mostrar detalles automáticamente
            if u != "Todos" and m != "Todos" and o != "Todos" and r != "Todos" and len(filtered) == 1:
                self.show_detail(filtered[0])
                # seleccionar en treeview la única fila
                self.tree.selection_set("0")
            else:
                # limpiar panel detalles
                self.clear_detail()
        finally:
            self._updating = False

    def on_tree_select(self, event):
        # Mostrar detalle del item seleccionado en el treeview
        sel = self.tree.selection()
        if not sel:
            return
        iid = sel[0]
        # el iid corresponde al índice en filtered en la llamada más reciente,
        # para mantener simple, recalculamos filtered con los filtros actuales.
        u = self.user_var.get()
        m = self.mission_var.get()
        o = self.objective_var.get()
        r = self.resource_var.get()

        def matches(rec):
            if u != "Todos" and rec["usuario"] != u: return False
            if m != "Todos" and rec["mision"] != m: return False
            if o != "Todos" and rec["objetivo"] != o: return False
            if r != "Todos" and rec["recurso"] != r: return False
            return True

        filtered = [rec for rec in self.data if matches(rec)]
        try:
            rec = filtered[int(iid)]
        except Exception:
            return
        self.show_detail(rec)

    def show_detail(self, rec):
        text = (
            f"Usuario: {rec.get('usuario')}\n"
            f"Misión: {rec.get('mision')}\n"
            f"Objetivo: {rec.get('objetivo')}\n"
            f"Recurso: {rec.get('recurso')}\n\n"
            f"Fecha: {rec.get('fecha')}\n"
            f"Hora: {rec.get('hora')}\n"
            f"Resultado: {rec.get('resultado')}\n\n"
            f"Notas:\n{rec.get('notas')}\n"
        )
        self.detail_text.config(state="normal")
        self.detail_text.delete("1.0", tk.END)
        self.detail_text.insert(tk.END, text)
        self.detail_text.config(state="disabled")

    def clear_detail(self):
        self.detail_text.config(state="normal")
        self.detail_text.delete("1.0", tk.END)
        self.detail_text.config(state="disabled")

# -----------------------
# Ejecutar app
# -----------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MissionFilterApp(root, data)
    root.mainloop()
