import flet as ft


class FletMVCView:
    def __init__(self):
        self.model = None
        self.controller = None

        self.page: ft.Page = None  # noqa

    def build(self, page: ft.Page) -> None:
        self.page = page

    def update(self, controls: list[ft.Control] | None = None) -> None:
        if self.page is not None:
            if controls is None:
                self.page.update()
            else:
                self.page.update(*controls)

    def open_dialog(self, dlg: ft.AlertDialog) -> None:
        self.page.dialog = dlg
        dlg.open = True
        self.update()

    def close(self, e: ft.ControlEvent = None) -> None:
        assert e is None or isinstance(e, ft.ControlEvent)

        self.page.window_close()

    def close_dialog(self, e: ft.ControlEvent = None) -> None:
        assert e is None or isinstance(e, ft.ControlEvent)

        self.page.dialog.open = False
        self.update()

    def change_theme_mode(self, mode) -> None:
        self.page.theme_mode = mode
        self.update()
