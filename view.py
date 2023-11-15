import flet as ft
from flet_core.connection import Connection

from mvc import MVCView


class SettingsView(MVCView):
    def __init__(self):
        super().__init__()

        self.switch = ft.Ref[ft.Switch]()
        self.dropdown = ft.Ref[ft.Dropdown]()
        self.textfield = ft.Ref[ft.TextField]()
        self.button = ft.Ref[ft.ElevatedButton]()
        self.column = ft.Ref[ft.Column]()

    def build(self, page):
        self.switch = ft.Switch(label="Dark mode", on_change=self.controller.change_mode)

        options = [ft.dropdown.Option(o) for o in self.model.options]
        self.dropdown = ft.Dropdown(options=options, key="dropdown", on_change=self.controller.dropdown_change)
        self.textfield = ft.TextField()
        self.button = ft.ElevatedButton(text="Close", on_click=self.controller.button_click)
        self.column = ft.Column(controls=[self.switch, self.dropdown, self.textfield, self.button])

        page.add(self.column)
