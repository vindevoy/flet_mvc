import flet as ft

from mvc import MVCController


class SettingsController(MVCController):
    @staticmethod
    def change_mode(e: ft.ControlEvent):
        p: ft.Page = e.page
        p.theme_mode = ft.ThemeMode.DARK if e.control.value else ft.ThemeMode.LIGHT
        p.update()

    def dropdown_change(self, e: ft.ControlEvent):
        dropdown: ft.Dropdown = e.control
        textfield: ft.TextField = self.view.textfield

        textfield.value = self.model.option_name(dropdown.value)
        # could use e.data also in this case
        textfield.update()

    def button_click(self, e: ft.ControlEvent):
        dlg = ft.AlertDialog(
            modal=True,
            actions=[
                ft.TextButton("Yes", on_click=self.close_application),
                ft.TextButton("No", on_click=self.close_dialog)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            title=ft.Text(f"Close the application ?")
        )

        e.page.dialog = dlg
        dlg.open = True
        e.page.update()

    @staticmethod
    def close_dialog(e: ft.ControlEvent):
        e.page.dialog.open = False
        e.page.update()

    @staticmethod
    def close_application(e: ft.ControlEvent):
        e.page.window_close()

#
# def _named_controls(page: ft.Control | ft.Page):
#     named = {}
#
#     try:
#         for control in page.controls:
#             if control.key not in [None, ""]:
#                 named[control.key] = control
#
#             named = {**named, **_named_controls(control)}
#             # add to the dict of this control, the dict of the controls deeper down the control tree
#     except AttributeError:
#         pass  # container does not have a controls property
#
#     return named
