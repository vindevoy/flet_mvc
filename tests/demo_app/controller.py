import flet as ft

from flet_mvc.controller import FletMVCController


class DemoController(FletMVCController):
    def change_mode(self, e: ft.ControlEvent):
        assert isinstance(e, ft.ControlEvent)

        self.change_theme_mode(ft.ThemeMode.DARK if e.control.value else ft.ThemeMode.LIGHT)

    def dropdown_change(self, e: ft.ControlEvent = None):  # You must have the ControlEvent as parameter
        assert isinstance(e, ft.ControlEvent)

        self.view.textfield.value = self.model.option_code(self.view.dropdown.value)
        self.refresh()

    def button_click(self, e: ft.ControlEvent = None):
        assert isinstance(e, ft.ControlEvent)

        dlg = ft.AlertDialog(
            modal=True,
            actions=[
                ft.TextButton("Yes", on_click=self.close_application),
                ft.TextButton("No", on_click=self.close_dialog)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            title=ft.Text(f"Close the application ?")
        )

        self.open_dialog(dlg)
