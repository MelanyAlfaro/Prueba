import tkinter as tk
from tkinter import ttk

# Datos de ejemplo
data = [
    {
        "usuario": "NeoTrek",
        "mision": "Reconexión satélite",
        "objetivo": "Diagnóstico general",
        "recurso": "Terminal portátil",
        "fecha": "2025-08-04",
        "hora": "14:35",
        "resultado": "Completado",
        "notas": "Operación sin inconvenientes"
    },
    {
        "usuario": "AstroVega",
        "mision": "Exploración cavernas",
        "objetivo": "Mapeo 3D",
        "recurso": "Drone XR",
        "fecha": "2025-08-05",
        "hora": "09:15",
        "resultado": "Pendiente",
        "notas": "Esperando condiciones óptimas"
    },
    {
        "usuario": "NeoTrek",
        "mision": "Instalación sistema energético",
        "objetivo": "Calibración nodos",
        "recurso": "Kit herramientas",
        "fecha": "2025-08-06",
        "hora": "16:50",
        "resultado": "Completado",
        "notas": "Revisión final completada"
    }
]

class MissionFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Filtro de Misiones - OrbitOps")
        self.root.geometry("950x500")
        self.root.configure(bg="#e6f0ff")

        style = ttk.Style()
        style.configure("TLabel", background="#e6f0ff", foreground="#003366", font=("Arial", 10))
        style.configure("TListbox", background="#cce0ff", foreground="#003366")
        style.configure("TFrame", background="#e6f0ff")
        
        # Variables de selección
        self.selected_user = None
        self.selected_mission = None
        self.selected_objective = None
        self.selected_resource = None

        # Frames para listas
        frame_lists = ttk.Frame(self.root)
        frame_lists.pack(pady=10, fill="x")

        self.user_listbox = self.create_listbox(frame_lists, "Usuarios", self.on_user_select)
        self.mission_listbox = self.create_listbox(frame_lists, "Misiones", self.on_mission_select)
        self.objective_listbox = self.create_listbox(frame_lists, "Objetivos", self.on_objective_select)
        self.resource_listbox = self.create_listbox(frame_lists, "Recursos", self.on_resource_select)

        self.populate_all_lists()

        # Frame para resultados
        self.result_label = ttk.Label(self.root, text="Seleccione un elemento en cada lista para ver los detalles",
                                      font=("Arial", 12, "bold"))
        self.result_label.pack(pady=20)

    def create_listbox(self, parent, title, command):
        frame = ttk.Frame(parent)
        frame.pack(side="left", padx=10, expand=True, fill="y")

        label = ttk.Label(frame, text=title, font=("Arial", 11, "bold"))
        label.pack(pady=5)

        listbox = tk.Listbox(frame, height=12, exportselection=False, bg="#cce0ff", fg="#003366",
                             font=("Arial", 10))
        listbox.pack(fill="y", expand=True)
        listbox.bind("<<ListboxSelect>>", command)

        return listbox

    def populate_all_lists(self):
        self.populate_list(self.user_listbox, sorted({d["usuario"] for d in data}))
        self.populate_list(self.mission_listbox, sorted({d["mision"] for d in data}))
        self.populate_list(self.objective_listbox, sorted({d["objetivo"] for d in data}))
        self.populate_list(self.resource_listbox, sorted({d["recurso"] for d in data}))

    def populate_list(self, listbox, items):
        listbox.delete(0, tk.END)
        for item in items:
            listbox.insert(tk.END, item)

    def on_user_select(self, event):
        selection = self.user_listbox.curselection()
        if selection:
            self.selected_user = self.user_listbox.get(selection[0])
        self.update_lists()

    def on_mission_select(self, event):
        selection = self.mission_listbox.curselection()
        if selection:
            self.selected_mission = self.mission_listbox.get(selection[0])
        self.update_lists()

    def on_objective_select(self, event):
        selection = self.objective_listbox.curselection()
        if selection:
            self.selected_objective = self.objective_listbox.get(selection[0])
        self.update_lists()

    def on_resource_select(self, event):
        selection = self.resource_listbox.curselection()
        if selection:
            self.selected_resource = self.resource_listbox.get(selection[0])
        self.update_lists()

    def update_lists(self):
        filtered = data
        if self.selected_user:
            filtered = [d for d in filtered if d["usuario"] == self.selected_user]
        if self.selected_mission:
            filtered = [d for d in filtered if d["mision"] == self.selected_mission]
        if self.selected_objective:
            filtered = [d for d in filtered if d["objetivo"] == self.selected_objective]
        if self.selected_resource:
            filtered = [d for d in filtered if d["recurso"] == self.selected_resource]

        if not self.selected_user:
            self.populate_list(self.user_listbox, sorted({d["usuario"] for d in filtered}))
        if not self.selected_mission:
            self.populate_list(self.mission_listbox, sorted({d["mision"] for d in filtered}))
        if not self.selected_objective:
            self.populate_list(self.objective_listbox, sorted({d["objetivo"] for d in filtered}))
        if not self.selected_resource:
            self.populate_list(self.resource_listbox, sorted({d["recurso"] for d in filtered}))

        # Si ya hay selección en todas las listas, mostrar resultado
        if all([self.selected_user, self.selected_mission, self.selected_objective, self.selected_resource]):
            for item in filtered:
                self.result_label.config(text=(
                    f"Fecha: {item['fecha']} | Hora: {item['hora']} | "
                    f"Resultado: {item['resultado']} | Notas: {item['notas']}"
                ))

if __name__ == "__main__":
    root = tk.Tk()
    app = MissionFilterApp(root)
    root.mainloop()
