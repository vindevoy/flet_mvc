from flet_mvc.controller import FletMVCController


class CountriesController(FletMVCController):
    def __init__(self):
        super().__init__()

    def show_home(self, _):  # _: instead of e:ft.ControlEvent
        self.goto("/")

    def show_data(self, _):  # _: instead of e:ft.ControlEvent
        self.goto(f"/country/{self.view.dropdown.value}")
