import flet as ft
from flet_core import RouteChangeEvent, TemplateRoute

from module import FletMVCModule
from route import FletMVCRoute


class FletMVCApplication:
    def __init__(self, title: str):
        """
        Constructor that creates a dummy page, which will later be detailed in the build method.
        Also creates the title of the application and the list of routes
        """
        self.title: str = title

        self.__page: ft.Page = None  # noqa
        self.__routes: list[FletMVCRoute] = []

    def add_route(self, path: str, module: FletMVCModule):
        # In each of the 3 parts, inject the app, so they all have a common parent
        module.model.app = self
        module.view.app = self
        module.controller.app = self

        route = FletMVCRoute(path=path, module=module)
        self.__routes.append(route)

    def run(self):
        ft.app(target=self.__build)

    def goto(self, path: str):
        self.__page.go(path)

    def update(self, controls: list[ft.Control] = None) -> None:
        """
        Update the view / page.  Either update it completely, or only the controls listed.

        :param controls: list[ft.Control] | None:
            The list of controls you want to be updated. If None, the whole view/page is updated.

        :return: None
        """

        if self.__page is not None:
            if controls is None:
                self.__page.update()
            else:
                self.__page.update(*controls)

    def open_dialog(self, dlg: ft.AlertDialog) -> None:
        """
        Open a dialog for the view/page.

        :param dlg: ft.AlertDialog:
            The dialog to be opened.

        :return: None
        """
        self.__page.dialog = dlg
        dlg.open = True
        self.update()

    def close_dialog(self, e: ft.ControlEvent) -> None:
        """
        Convenience method that passes the close_dialog to the view.

        This method is supposed to be called by the controller.  It therefore has the e (ControlEvent) as parameter.
        You can use this on a button, for example, using the on_click method where you write
        on_click=self.controller.close_dialog  (pass the function, do not call the function)

        :param e: ft.ControlEvent:
            The ControlEvent from Flet that triggers this call.

        :return: None
        """
        assert isinstance(e, ft.ControlEvent)

        self.__page.close_dialog()

    def close_application(self, e: ft.ControlEvent) -> None:
        """
        Closes the application as it closes the view with window_close().  This is to be called from the controller.

        :param e: ft.ControlEvent:
            The ControlEvent from Flet that triggers this call.

        :return: None
        """
        assert isinstance(e, ft.ControlEvent)

        self.__page.window_close()

    def change_theme_mode(self, mode) -> None:
        """
        Change the theme mode from light to dark, or vice versa.

        :param mode: ft.ThemeMode:
            The mode to change the theme mode into.
            This should be given as ft.ThemeMode.DARK or ft.ThemeMode.LIGHT.

        :return: None
        """
        self.__page.theme_mode = mode
        self.update()

    def __build(self, page: ft.Page):
        self.__page = page
        self.__page.title = self.title

        self.__page.on_route_change = self.__route_change
        self.__page.go(self.__page.route)

    @staticmethod
    def __inject_params(path: str, route: TemplateRoute):
        params = []
        elements = path.split("/")

        for elem in elements:
            if elem.startswith(":"):
                params.append(route.__getattribute__(elem[1:]))

        return params

    def __route_change(self, e: RouteChangeEvent):
        self.__page = e.page
        self.__page.views.clear()

        for route in self.__routes:
            if route.is_dynamic():
                template_route = TemplateRoute(self.__page.route)

                if template_route.match(route.path):
                    params = self.__inject_params(route.path, template_route)
                    self.__page.views.append(route.module.view.build(*params))

            elif route.path == e.page.route:
                self.__page.views.append(route.module.view.build())

        self.update()
