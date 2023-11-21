from flet_mvc.view import FletMVCView
import flet as ft


class CountriesListView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.dropdown = ft.Ref[ft.Dropdown]()
        self.button = ft.Ref[ft.ElevatedButton]()
        self.view = ft.Ref[ft.View]()

    def build(self) -> ft.View:
        options = [ft.dropdown.Option(c) for c in self.model.get_country_list()]
        self.dropdown = ft.Dropdown(ref=self.dropdown, col=3, options=options, label="Select a country")
        self.button = ft.ElevatedButton(ref=self.button, col=2, text="See data", on_click=self.controller.show_data)
        self.view = ft.View(controls=[self.dropdown, self.button])

        return self.view


class CountryDetailView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.text = ft.Ref[ft.Text]()
        self.datatable = ft.Ref[ft.DataTable]()
        self.row = ft.Ref[ft.ResponsiveRow]()
        self.button = ft.Ref[ft.ElevatedButton]()
        self.view = ft.Ref[ft.View]()

    def build(self, country: str) -> ft.View:
        self.text = ft.Text(ref=self.text, value=f"Life expectancy for {country}")

        cols = [ft.DataColumn(ft.Text("Year"), numeric=True),
                ft.DataColumn(ft.Text("Life Expectancy (years)"), numeric=True)]

        rows = [ft.DataRow(cells=[
            ft.DataCell(ft.Text(data["year"])),
            ft.DataCell(ft.Text(data["life_expect"]))]
            ) for data in self.model.get_country_life_expectancy(country_name=country)]

        self.datatable = ft.DataTable(ref=self.datatable, columns=cols, rows=rows)
        self.row = ft.ResponsiveRow(controls=[self.datatable])
        self.button = ft.ElevatedButton(ref=self.button, col=2, text="Home", on_click=self.controller.show_home)
        self.view = ft.View(controls=[self.text, self.row, self.button])

        return self.view
