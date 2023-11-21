import flet as ft

from flet_mvc.view import FletMVCView


class ContactsView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.datatable = ft.Ref[ft.DataTable]()
        self.button = ft.Ref[ft.ElevatedButton]()
        self.view = ft.Ref[ft.View]()

    def build(self) -> ft.View:
        self.button = ft.ElevatedButton(ref=self.button, col=2, text="Close",
                                        on_click=self.controller.close_application)
        self.view = ft.View(controls=[self.button])

        return self.view
