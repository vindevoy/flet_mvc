import flet as ft


class FletMVCController:
    def __init__(self):
        """
        Constructor to set the parent app which will be filled out when the MVC module is added to the app.
        It also sets the 2 other components in the MVC pattern.  That will be filled out when the 3 are combined
        in the MVC module's constructor.
        """
        self.app = None
        self.model = None
        self.view = None

    def goto(self, path: str):
        """
        Convenience method to pass from the level of the controller to the level of the application with the page.
        For full documentation, see the same method on the app (application) level.

        :param path: str:

        :return: None
        """
        self.app.goto(path=path)

    def update(self, controls: list[ft.Control] = None) -> None:
        """
        Convenience method to pass from the level of the controller to the level of the application with the page.
        For full documentation, see the same method on the app (application) level.

        :param controls: list[ft.Control] | None:

        :return: None
        """
        self.app.update(controls=controls)

    def open_dialog(self, dlg: ft.AlertDialog) -> None:
        """
        Convenience method to pass from the level of the controller to the level of the application with the page.
        For full documentation, see the same method on the app (application) level.

        :param dlg: ft.AlertDialog:

        :return: None
        """
        self.app.open_dialog(dlg=dlg)

    def close_dialog(self, e: ft.ControlEvent) -> None:
        """
        Convenience method to pass from the level of the controller to the level of the application with the page.
        For full documentation, see the same method on the app (application) level.

        :param e: ft.ControlEvent:

        :return: None
        """
        self.app.close_dialog(e=e)

    def close_application(self, e: ft.ControlEvent) -> None:
        """
        Convenience method to pass from the level of the controller to the level of the application with the page.
        For full documentation, see the same method on the app (application) level.

        :param e: ft.ControlEvent:

        :return: None
        """
        self.app.close_application(e=e)

    def change_theme_mode(self, mode: ft.ThemeMode) -> None:
        """
        Convenience method to pass from the level of the controller to the level of the application with the page.
        For full documentation, see the same method on the app (application) level.

        :param mode: str:

        :return: None
        """
        self.app.change_theme_mode(mode=mode)
