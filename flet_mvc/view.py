class FletMVCView:
    def __init__(self):
        """
        Constructor that creates the 2 other components in the MVC pattern.  They will be set by the FletMVCApp.

        It also creates a page property that will be used to for instance update the page.
        """
        self.app = None
        self.model = None
        self.controller = None

    # def update(self, controls: list[ft.Control] = None) -> None:
    #     """
    #     Update the view / page.  Either update it completely, or only the controls listed.
    #
    #     :param controls: list[ft.Control] | None:
    #         The list of controls you want to be updated. If None, the whole view/page is updated.
    #
    #     :return: None
    #     """
    #
    #     if self.page is not None:
    #         if controls is None:
    #             self.page.update()
    #         else:
    #             self.page.update(*controls)
    #
    # def open_dialog(self, dlg: ft.AlertDialog) -> None:
    #     """
    #     Open a dialog for the view/page.
    #
    #     :param dlg: ft.AlertDialog:
    #         The dialog to be opened.
    #
    #     :return: None
    #     """
    #     self.page.dialog = dlg
    #     dlg.open = True
    #     self.update()
    #
    # def close(self, e: ft.ControlEvent) -> None:
    #     """
    #     Closes the application as it closes the view with window_close().  This is to be called from the controller.
    #
    #     :param e: ft.ControlEvent:
    #         The ControlEvent from Flet that triggers this call.
    #
    #     :return: None
    #     """
    #     assert isinstance(e, ft.ControlEvent)
    #
    #     self.page.window_close()
    #
    # def close_dialog(self, e: ft.ControlEvent) -> None:
    #     """
    #     Closes the dialog that is opened for this page / view.  This is to be called from the controller.
    #
    #     :param e: ft.ControlEvent:
    #         The ControlEvent from Flet that triggers this call.
    #
    #     :return: None
    #     """
    #     assert isinstance(e, ft.ControlEvent)
    #
    #     self.page.dialog.open = False
    #     self.update()
    #
    # def change_theme_mode(self, mode) -> None:
    #     """
    #     Change the theme mode from light to dark, or vice versa.
    #
    #     :param mode: ft.ThemeMode:
    #         The mode to change the theme mode into.
    #         This should be given as ft.ThemeMode.DARK or ft.ThemeMode.LIGHT.
    #
    #     :return: None
    #     """
    #     self.page.theme_mode = mode
    #     self.update()
