import json
import wx
from typing import List, Dict, Any, Set

# -----------------------------
# Modelo simple para un registro
# -----------------------------
# Cada registro debe tener las llaves:
#   user: str
#   mission: str
#   objectives: List[str]
#   resources: List[str]
#   date: "YYYY-MM-DD"
#   time: "HH:MM" o ""
#   result: str
#   notes: str

SampleData: List[Dict[str, Any]] = [
    {
        "user": "NeoTrek",
        "mission": "Reconexión satélite A3",
        "objectives": ["Diagnóstico general", "Reinicio seguro"],
        "resources": ["Terminal portátil", "Kit conexión", "Dron-12"],
        "date": "2025-08-04",
        "time": "14:35",
        "result": "Completado",
        "notes": "#urgente Verificar enlace X23; código CMD_RESTART"
    },
    {
        "user": "AdaPilot",
        "mission": "Patrullaje orbital B",
        "objectives": ["Monitoreo térmico", "Registro telemetría"],
        "resources": ["Dron-12", "Sensor T"],
        "date": "2025-08-05",
        "time": "09:10",
        "result": "ok",
        "notes": "Trayectoria estable"
    },
    {
        "user": "NeoTrek",
        "mission": "Patrullaje orbital B",
        "objectives": ["Registro telemetría"],
        "resources": ["Sensor T"],
        "date": "2025-08-06",
        "time": "10:05",
        "result": "ok",
        "notes": "Turno extendido"
    },
    {
        "user": "VeraOps",
        "mission": "Exploración caverna C7",
        "objectives": ["Mapeo lidar"],
        "resources": ["Rover-C", "Lidar-X"],
        "date": "2025-08-07",
        "time": "",
        "result": "Pendiente",
        "notes": "Esperando ventana de acceso"
    },
]

# -----------------------------
# Utilidades
# -----------------------------

def unique_sorted(items: List[str]) -> List[str]:
    return sorted(set(items), key=lambda x: x.lower())


def extract_universe(records: List[Dict[str, Any]]):
    users = unique_sorted([r["user"] for r in records])
    missions = unique_sorted([r["mission"] for r in records])
    objectives = unique_sorted(obj for r in records for obj in r["objectives"])
    resources = unique_sorted(res for r in records for res in r["resources"])
    return users, missions, objectives, resources


# -----------------------------
# GUI
# -----------------------------

class PointEFrame(wx.Frame):
    def __init__(self, records: List[Dict[str, Any]]):
        super().__init__(None, title="OrbitOps — Punto e (wxPython)", size=(1100, 680))
        self.records: List[Dict[str, Any]] = records[:]  # copia
        self.filtered: List[Dict[str, Any]] = records[:]
        self.selections: Dict[str, Any] = {"user": None, "mission": None, "objective": None, "resource": None}

        self._build_ui()
        self.Center()
        self.Show()

    # Paleta azul
    def _palette(self):
        return {
            "bg": wx.Colour(235, 245, 255),
            "bg_card": wx.Colour(220, 235, 255),
            "accent": wx.Colour(25, 90, 160),
            "accent_light": wx.Colour(100, 155, 220),
            "text": wx.Colour(15, 35, 60),
            "border": wx.Colour(160, 195, 235),
        }

    def _build_ui(self):
        pal = self._palette()
        panel = wx.Panel(self)
        panel.SetBackgroundColour(pal["bg"]) 

        # Menu
        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        open_item = file_menu.Append(wx.ID_OPEN, "&Cargar…\tCtrl+O", "Cargar archivo JSON parseado")
        reset_item = file_menu.Append(wx.ID_ANY, "&Reiniciar filtros\tCtrl+R")
        menubar.Append(file_menu, "Archivo")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.on_open, open_item)
        self.Bind(wx.EVT_MENU, self.on_reset, reset_item)

        root = wx.BoxSizer(wx.VERTICAL)

        header = wx.Panel(panel)
        header.SetBackgroundColour(pal["bg"]) 
        hsz = wx.BoxSizer(wx.HORIZONTAL)
        title = wx.StaticText(header, label="PUNTO e — Filtro cruzado: Usuarios / Misiones / Objetivos / Recursos")
        title.SetForegroundColour(pal["accent"])
        font = title.GetFont()
        font.PointSize += 3
        font.MakeBold()
        title.SetFont(font)
        hsz.Add(title, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 8)
        header.SetSizer(hsz)
        root.Add(header, 0, wx.EXPAND)

        body = wx.Panel(panel)
        body.SetBackgroundColour(pal["bg"]) 
        grid = wx.FlexGridSizer(rows=2, cols=4, vgap=8, hgap=8)
        grid.AddGrowableCol(0, 1)
        grid.AddGrowableCol(1, 1)
        grid.AddGrowableCol(2, 1)
        grid.AddGrowableCol(3, 1)
        grid.AddGrowableRow(1, 1)

        def make_listbox(parent, title_text):
            box = wx.Panel(parent)
            box.SetBackgroundColour(pal["bg"]) 
            vsz = wx.BoxSizer(wx.VERTICAL)
            lbl = wx.StaticText(box, label=title_text)
            lbl.SetForegroundColour(pal["accent"])
            lbl_font = lbl.GetFont()
            lbl_font.MakeBold()
            lbl.SetFont(lbl_font)

            lb_panel = wx.Panel(box)
            lb_panel.SetBackgroundColour(pal["bg_card"]) 
            lb_panel.SetWindowStyle(wx.SIMPLE_BORDER)
            lb_panel.SetForegroundColour(pal["text"])
            lb_sz = wx.BoxSizer(wx.VERTICAL)
            lb = wx.ListBox(lb_panel, style=wx.LB_SINGLE)
            lb.SetBackgroundColour(wx.Colour(245, 250, 255))
            lb_sz.Add(lb, 1, wx.EXPAND | wx.ALL, 6)
            lb_panel.SetSizer(lb_sz)

            vsz.Add(lbl, 0, wx.LEFT | wx.RIGHT | wx.TOP, 4)
            vsz.Add(lb_panel, 1, wx.EXPAND | wx.ALL, 0)
            box.SetSizer(vsz)
            return box, lb

        # Encabezados fila 0
        grid.Add(make_listbox(body, "Usuarios")[0], 0, wx.EXPAND)
        grid.Add(make_listbox(body, "Misiones")[0], 0, wx.EXPAND)
        grid.Add(make_listbox(body, "Objetivos")[0], 0, wx.EXPAND)
        grid.Add(make_listbox(body, "Recursos")[0], 0, wx.EXPAND)

        # Fila 1 con listboxes reales (necesitamos referencias)
        self.users_box, self.users_lb = make_listbox(body, "Usuarios")
        self.missions_box, self.missions_lb = make_listbox(body, "Misiones")
        self.objectives_box, self.objectives_lb = make_listbox(body, "Objetivos")
        self.resources_box, self.resources_lb = make_listbox(body, "Recursos")

        grid.Add(self.users_box, 1, wx.EXPAND)
        grid.Add(self.missions_box, 1, wx.EXPAND)
        grid.Add(self.objectives_box, 1, wx.EXPAND)
        grid.Add(self.resources_box, 1, wx.EXPAND)

        body.SetSizer(grid)
        root.Add(body, 1, wx.EXPAND | wx.ALL, 12)

        # Panel de detalles
        details = wx.Panel(panel)
        details.SetBackgroundColour(pal["bg_card"]) 
        details.SetWindowStyle(wx.SIMPLE_BORDER)
        dsz = wx.BoxSizer(wx.HORIZONTAL)

        def make_field(label_text):
            pnl = wx.Panel(details)
            pnl.SetBackgroundColour(pal["bg_card"]) 
            vs = wx.BoxSizer(wx.VERTICAL)
            lab = wx.StaticText(pnl, label=label_text)
            lab.SetForegroundColour(pal["accent_light"])
            lab_font = lab.GetFont()
            lab_font.MakeBold()
            lab.SetFont(lab_font)
            val = wx.StaticText(pnl, label="—")
            val.SetForegroundColour(pal["text"])
            vs.Add(lab, 0, wx.BOTTOM, 2)
            vs.Add(val, 0, wx.BOTTOM, 0)
            pnl.SetSizer(vs)
            return pnl, val

        self.date_pnl, self.date_val = make_field("Fecha")
        self.time_pnl, self.time_val = make_field("Hora")
        self.result_pnl, self.result_val = make_field("Resultado")
        self.notes_pnl, self.notes_val = make_field("Notas")

        dsz.Add(self.date_pnl, 0, wx.ALL, 10)
        dsz.Add(self.time_pnl, 0, wx.ALL, 10)
        dsz.Add(self.result_pnl, 0, wx.ALL, 10)
        dsz.Add(self.notes_pnl, 1, wx.ALL | wx.EXPAND, 10)

        details.SetSizer(dsz)
        root.Add(details, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 12)

        panel.SetSizer(root)

        # StatusBar
        self.CreateStatusBar()
        self.SetStatusText("Listo")

        # Eventos
        for lb, key in [
            (self.users_lb, "user"),
            (self.missions_lb, "mission"),
            (self.objectives_lb, "objective"),
            (self.resources_lb, "resource"),
        ]:
            lb.Bind(wx.EVT_LISTBOX, lambda evt, k=key: self.on_pick(evt, k))

        # Inicializar contenido
        self.populate_all()

    # -----------------------------
    # Carga y reseteo
    # -----------------------------
    def on_open(self, _evt):
        with wx.FileDialog(self, "Cargar archivo JSON", wildcard="JSON (*.json)|*.json", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if not isinstance(data, list):
                        raise ValueError("El JSON debe ser una lista de registros")
                    self.records = data
                    self.on_reset(None)
                    self.SetStatusText(f"Archivo cargado: {path}")
                except Exception as e:
                    wx.MessageBox(f"Error al cargar JSON:\n{e}", "Error", wx.ICON_ERROR | wx.OK)

    def on_reset(self, _evt):
        self.selections = {"user": None, "mission": None, "objective": None, "resource": None}
        self.filtered = self.records[:]
        self.populate_all()
        self.show_details(None)
        self.SetStatusText("Filtros reiniciados")

    # -----------------------------
    # Poblado y filtrado
    # -----------------------------
    def populate_all(self):
        # Construir universo segun filtro actual
        self.apply_filters()
        users, missions, objectives, resources = self.compute_available_options()

        def load(lb: wx.ListBox, items: List[str], selected: str | None):
            cur = lb.GetStringSelection()
            lb.Clear()
            lb.AppendItems(items)
            if selected and selected in items:
                lb.SetStringSelection(selected)
            elif cur and cur in items:
                lb.SetStringSelection(cur)

        load(self.users_lb, users, self.selections["user"])
        load(self.missions_lb, missions, self.selections["mission"])
        load(self.objectives_lb, objectives, self.selections["objective"])
        load(self.resources_lb, resources, self.selections["resource"])

        self.SetStatusText(f"Registros compatibles: {len(self.filtered)}")
        self.maybe_show_details()

    def apply_filters(self):
        sel = self.selections
        def match(r: Dict[str, Any]) -> bool:
            if sel["user"] and r["user"] != sel["user"]:
                return False
            if sel["mission"] and r["mission"] != sel["mission"]:
                return False
            if sel["objective"] and sel["objective"] not in r["objectives"]:
                return False
            if sel["resource"] and sel["resource"] not in r["resources"]:
                return False
            return True
        self.filtered = [r for r in self.records if match(r)]

    def compute_available_options(self):
        users: Set[str] = set()
        missions: Set[str] = set()
        objectives: Set[str] = set()
        resources: Set[str] = set()
        for r in self.filtered:
            users.add(r["user"]) 
            missions.add(r["mission"]) 
            for o in r["objectives"]:
                objectives.add(o)
            for res in r["resources"]:
                resources.add(res)
        return (sorted(users, key=str.lower),
                sorted(missions, key=str.lower),
                sorted(objectives, key=str.lower),
                sorted(resources, key=str.lower))

    def on_pick(self, evt: wx.CommandEvent, key: str):
        val = evt.GetString() if evt.GetEventObject().GetSelection() != wx.NOT_FOUND else None
        self.selections[key] = val
        self.populate_all()

    # -----------------------------
    # Detalles de la misión
    # -----------------------------
    def maybe_show_details(self):
        # Mostrar detalles cuando hay selección en TODAS las listas
        if all(self.selections.values()):
            # Buscar el primer registro que cumpla todo
            for r in self.filtered:
                if (self.selections["objective"] in r["objectives"] and
                    self.selections["resource"] in r["resources"]):
                    self.show_details(r)
                    return
        self.show_details(None)

    def show_details(self, r: Dict[str, Any] | None):
        if r is None:
            self.date_val.SetLabel("—")
            self.time_val.SetLabel("—")
            self.result_val.SetLabel("—")
            self.notes_val.SetLabel("—")
        else:
            self.date_val.SetLabel(r.get("date", "—"))
            self.time_val.SetLabel(r.get("time", "—") or "—")
            self.result_val.SetLabel(r.get("result", "—"))
            self.notes_val.SetLabel(r.get("notes", "—"))
        self.Layout()


class App(wx.App):
    def OnInit(self):
        frame = PointEFrame(SampleData)
        frame.SetIcon(wx.ArtProvider.GetIcon(wx.ART_INFORMATION, wx.ART_FRAME_ICON, (16, 16)))
        return True


if __name__ == "__main__":
    app = App(False)
    app.MainLoop()
