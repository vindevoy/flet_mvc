import flet as ft
from flet_core import RouteChangeEvent, TemplateRoute

from flet_mvc.module import FletMVCModule
from flet_mvc.route import FletMVCRoute


class FletMVCApplication:
    def __init__(self, title: str, window_width: int = 1600, window_height: int = 900):
        """
        Constructor that creates a dummy page, which will later be detailed in the build method.
        Also creates the basic properties of the application and the list of routes
        """
        self.title: str = title
        self.window_width = window_width
        self.window_height = window_height

        self.__page: ft.Page = None  # noqa
        self.__routes: list[FletMVCRoute] = []

    def add_route(self, path: str, module: FletMVCModule) -> None:
        """
        Create a route in the application to an MVC module containing a model, a view and a controller.

        :param path: str
            The path on which this route will listen.  You will see this if the application is running in a browser,
            but you will not see it in a desktop application.

        :param module: FletMVCModule
            A FletMVCModule, which has already combined the 3 parts of an MVC pattern component.

        :return: None
        """
        # In each of the 3 parts, inject the app, so they all have a common parent
        module.model.app = self
        module.view.app = self
        module.controller.app = self

        # add the new route
        route = FletMVCRoute(path=path, module=module)
        self.__routes.append(route)

    def run(self):
        """
        This is the main method that must be run to start the application from the main.py.

        :return: None
        """
        ft.app(target=self.__build)

    def goto(self, path: str):
        """
        Go to another page in the web browser, or load another screen in a desktop application.

        :param path: str:
            The path to which the application must go.  In a web browser, this will load a new page.
            In a desktop application, this will change the screen immediately.

        :return: None
        """
        self.__page.go(path)

    def update(self, controls: list[ft.Control] = None) -> None:
        """
        Update the page.  Either update it completely, or only the controls listed.

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
        Open a dialog in the page.

        :param dlg: ft.AlertDialog:
            The dialog to be opened.

        :return: None
        """
        self.__page.dialog = dlg
        dlg.open = True
        self.update()

    def close_dialog(self, e: ft.ControlEvent) -> None:
        """
        Close an opened dialog in the page.
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
        Closes the application as it closes the page with window_close().  This will only work in a desktop application.

        :param e: ft.ControlEvent:
            The ControlEvent from Flet that triggers this call.

        :return: None
        """
        assert isinstance(e, ft.ControlEvent)

        self.__page.window_close()

    def change_theme_mode(self, mode: ft.ThemeMode) -> None:
        """
        Change the theme mode from light to dark, or vice versa.

        :param mode: ft.ThemeMode:
            The mode to change the theme mode into.
            This should be given as ft.ThemeMode.DARK or ft.ThemeMode.LIGHT.

        :return: None
        """
        self.__page.theme_mode = mode
        self.update()

    def __build(self, page: ft.Page) -> None:
        """
        This method must be called by the run() method (only).  It will pass the page object from the flet.app target.
        This page object is kept as we will need it to update it each time we trigger an event.

        :param page: flet.Page:
            Passed by the run() method.

        :return: None
        """
        self.__page = page
        self.__page.title = self.title

        self.__page.window_width = self.window_width
        self.__page.window_height = self.window_height

        self.__page.on_route_change = self.__route_change
        self.__page.go(self.__page.route)

    @staticmethod
    def __inject_params(path: str, route: TemplateRoute) -> list[str]:
        """
        Private method to inject the parameters from the URL into the build.
        For example, path is declared as /countries/:country ID and the route is passed as /countries/Belgium,
        then "Belgium" will be parsed into the first parameter.

        :param path:  str
            The path as defined in the router.  It can contain parameters.

        :param route:  TemplateRoute
            The route demanded.  Normally, all the params will be filled out, and they are parsed into a list.

        :return: list[str]
            The list of strings that are parsed from the parameters in the definition of the route,
            and the URL containing the values.
        """
        params = []
        elements = path.split("/")

        for elem in elements:
            if elem.startswith(":"):
                params.append(route.__getattribute__(elem[1:]))

        return params

    def __route_change(self, e: RouteChangeEvent) -> None:
        """
        Event handler to handle the change of the route in the application, cause by an app.goto().

        :param e: RouteChangeEvent
            The event that will be passed when we have the change of the route

        :return: None
        """
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
