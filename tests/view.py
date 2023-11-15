import flet as ft

from flet_mvc.view import FletMVCView


class DemoView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.switch = ft.Ref[ft.Switch]()
        self.dropdown = ft.Ref[ft.Dropdown]()
        self.textfield = ft.Ref[ft.TextField]()
        self.button = ft.Ref[ft.ElevatedButton]()
        self.column = ft.Ref[ft.Column]()

    def build(self, page) -> None:
        super().build(page=page)

        self.switch = ft.Switch(ref=self.switch,
                                label="Dark mode",
                                on_change=self.controller.change_mode)
        self.dropdown = ft.Dropdown(ref=self.dropdown,
                                    options=[ft.dropdown.Option(o) for o in self.model.options],
                                    on_change=self.controller.dropdown_change)
        self.textfield = ft.TextField(ref=self.textfield)
        self.button = ft.ElevatedButton(ref=self.button,
                                        text="Close",
                                        on_click=self.controller.button_click)
        self.column = ft.Column(ref=self.column,
                                controls=[self.switch, self.dropdown, self.textfield, self.button])

        self.page.add(self.column)
