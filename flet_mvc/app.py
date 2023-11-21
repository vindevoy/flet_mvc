import flet as ft
from flet_core import RouteChangeEvent, TemplateRoute

from module import FletMVCModule
from route import FletMVCRoute


class FletMVCApplication:
    def __init__(self, title: str):
        self.page: ft.Page = None  # noqa
        self.title = title

        self.routes: list[FletMVCRoute] = []

    def add_route(self, path: str, module: FletMVCModule):
        module.model.app = self
        module.view.app = self
        module.controller.app = self

        route = FletMVCRoute(path=path, module=module)
        self.routes.append(route)

    def goto(self, path: str):
        self.page.go(path)

    def route_change(self, e: RouteChangeEvent):
        self.page = e.page

        self.page.views.clear()

        for route in self.routes:
            if route.is_dynamic():
                template_route = TemplateRoute(self.page.route)

                if template_route.match(route.path):
                    print(route.path)
                    print(template_route.__getattribute__("country_name"))

                    params = self.__inject_params(route.path, template_route)
                    print(params)
                    self.page.views.append(route.module.view.build(*params))

            elif route.path == e.page.route:
                self.page.views.append(route.module.view.build())

        self.page.update()

    @staticmethod
    def __inject_params(path: str, route: TemplateRoute):
        params = []
        elements = path.split("/")

        for elem in elements:
            if elem.startswith(":"):
                params.append(route.__getattribute__(elem[1:]))

        return params

    def build(self, page: ft.Page):
        print(page.route)

        self.page = page
        self.page.title = self.title

        self.page.on_route_change = self.route_change
        self.page.go(self.page.route)

    def run(self):
        ft.app(target=self.build)
