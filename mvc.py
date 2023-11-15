import flet as ft


class MVCModel:
    def __init__(self):
        self.controller = None
        self.view = None


class MVCView:
    def __init__(self):
        self.model = None
        self.controller = None

        self.page: ft.Page = None  # noqa

    def build(self, page):
        self.page = page

    def update(self, controls: list[ft.Control] | None = None):
        if self.page is not None:
            if controls is None:
                self.page.update()
            else:
                self.page.update(*controls)

    def open_dialog(self, dlg: ft.AlertDialog):
        self.page.dialog = dlg
        dlg.open = True
        self.update()

    def close(self, e: ft.ControlEvent = None):
        assert e is None or isinstance(e, ft.ControlEvent)

        self.page.window_close()

    def close_dialog(self, e: ft.ControlEvent = None):
        assert e is None or isinstance(e, ft.ControlEvent)

        self.page.dialog.open = False
        self.update()

    def change_theme_mode(self, mode):
        self.page.theme_mode = mode
        self.update()


class MVCController:
    def __init__(self):
        self.model = None
        self.view = None

    def update_view(self, controls: list[ft.Control] | None = None):
        self.view.update(controls)

    def open_dialog(self, dlg: ft.AlertDialog):
        self.view.open_dialog(dlg)

    def close_dialog(self, e: ft.ControlEvent = None):
        assert e is None or isinstance(e, ft.ControlEvent)

        self.view.close_dialog()

    def close_application(self, e: ft.ControlEvent = None):
        assert e is None or isinstance(e, ft.ControlEvent)

        self.view.close()


class MVCLinker:
    def __init__(self, model_class: MVCModel.__class__,
                 view_class: MVCView.__class__, controller_class: MVCController.__class__):
        self.model = model_class()
        self.view = view_class()
        self.controller = controller_class()

        self.model.controller = self.controller
        self.model.view = self.view

        self.view.model = self.model
        self.view.controller = self.controller

        self.controller.model = self.model
        self.controller.view = self.view

    def build(self, page):
        self.view.build(page)
