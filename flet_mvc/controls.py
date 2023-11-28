from typing import Callable

import flet as ft


class Controls:
    @classmethod
    def build_datatable(cls, ref: ft.Ref, columns: dict, data: list, on_select_changed: Callable):
        cols = [ft.DataColumn(ft.Text(key)) for key in columns.keys()]
        fields = columns.values()
        rows = [ft.DataRow(
            cells=[ft.DataCell(ft.Text(getattr(rec, fld))) for fld in fields],
            on_select_changed=on_select_changed
        ) for rec in data]

        return ft.DataTable(ref=ref, columns=cols, rows=rows)  # TODO: full width
