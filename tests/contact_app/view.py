import flet as ft

from flet_mvc.view import FletMVCView


class ContactsListView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.datatable = ft.Ref[ft.DataTable]()
        self.button = ft.Ref[ft.ElevatedButton]()
        self.view = ft.Ref[ft.View]()

    def build(self) -> ft.View:
        data = self.model.get_all()

        cols = [ft.DataColumn(ft.Text(c)) for c in ["ID", "Firstname", "Lastname", "Login"]]
        rows = []

        for rec in data:
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(rec.id)),
                    ft.DataCell(ft.Text(rec.firstname)),
                    ft.DataCell(ft.Text(rec.lastname)),
                    ft.DataCell(ft.Text(rec.login))
                ],
            )

            rows.append(row)

        self.datatable = ft.DataTable(columns=cols, rows=rows, expand=True)  # TODO: full width
        self.button = ft.ElevatedButton(ref=self.button, col=2, text="Close",
                                        on_click=self.controller.close_application)
        self.view = ft.View(controls=[self.datatable, self.button])

        return self.view
