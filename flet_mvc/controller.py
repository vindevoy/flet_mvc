class FletMVCController:
    def __init__(self):
        """
        Constructor that creates the 2 other components in the MVC pattern.  They will be set by the FletMVCApp.
        """
        self.app = None
        self.model = None
        self.view = None

    def goto(self, path: str):
        self.app.goto(path=path)

    # def update_view(self, controls: list[ft.Control] = None) -> None:
    #     """
    #     Convenience method that passes the update to the view.
    #     When no controls are specified, the whole page will be updated.  Otherwise, just the listed controls.
    #
    #     :param controls: list[ft.Control] | None:
    #         The list of controls you want to be updated.  If this list is None, the whole page will be updated.
    #
    #     :return: None
    #     """
    #     self.view.update(controls)
    #
    # def open_dialog(self, dlg: ft.AlertDialog) -> None:
    #     """
    #     Convenience method that passes the open_dialog to the view.
    #
    #     :param dlg: ft.AlertDialog:
    #         The dialog to open.
    #
    #     :return: None
    #     """
    #     self.view.open_dialog(dlg)
    #
    # def close_dialog(self, e: ft.ControlEvent) -> None:
    #     """
    #     Convenience method that passes the close_dialog to the view.
    #
    #     This method is supposed to be called by the controller.  It therefore has the e (ControlEvent) as parameter.
    #     You can use this on a button, for example, using the on_click method where you write
    #     on_click=self.controller.close_dialog  (pass the function, do not call the function)
    #
    #     :param e: ft.ControlEvent:
    #         The ControlEvent from Flet that triggers this call.
    #
    #     :return: None
    #     """
    #     assert isinstance(e, ft.ControlEvent)
    #
    #     self.view.close_dialog(e)
    #
    # def close_application(self, e: ft.ControlEvent) -> None:
    #     """
    #     Convenience method that passes the close to the view.
    #
    #     This method is supposed to be called by the controller.  It therefore has the e (ControlEvent) as parameter.
    #     You can use this on a button, for example, using the on_click method where you write
    #     on_click=self.controller.close_application  (pass the function, do not call the function)
    #
    #     :param e: ft.ControlEvent:
    #         The ControlEvent from Flet that triggers this call.
    #
    #     :return: None
    #     """
    #     assert isinstance(e, ft.ControlEvent)
    #
    #     self.view.close(e)
