import flet as ft


class FletMVCController:
    def __init__(self):
        self.model = None
        self.view = None

    def update_view(self, controls: list[ft.Control] | None = None) -> None:
        self.view.update(controls)

    def open_dialog(self, dlg: ft.AlertDialog) -> None:
        self.view.open_dialog(dlg)

    def close_dialog(self, e: ft.ControlEvent = None) -> None:
        assert e is None or isinstance(e, ft.ControlEvent)

        self.view.close_dialog()

    def close_application(self, e: ft.ControlEvent = None) -> None:
        assert e is None or isinstance(e, ft.ControlEvent)

        self.view.close()
