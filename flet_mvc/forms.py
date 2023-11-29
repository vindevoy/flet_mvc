from typing import Callable

import flet as ft


class Forms:
    @classmethod
    def title(cls, title: str):
        title_size = 28
        title_color = ft.colors.BLUE_900

        icon = ft.Icon(ft.icons.CONTACT_PAGE, size=title_size, color=title_color)
        txt_title = ft.Text(title, size=title_size, weight=ft.FontWeight.W_600, color=title_color)

        return ft.Row(controls=[icon, txt_title], col=12)

    @classmethod
    def information_text(cls, ref: ft.Ref, col_width: int = 8):
        return ft.TextField(ref=ref, disabled=True, visible=False, value="", col=col_width, height=32,
                            content_padding=ft.padding.only(left=10, top=0, bottom=0, right=10))

    @classmethod
    def right_aligned_row(cls, controls: list[ft.Control]):
        return ft.ResponsiveRow(controls=controls, alignment=ft.MainAxisAlignment.END)

    @classmethod
    def new_button(cls, ref: ft.Ref, call_on_click: Callable):
        return cls._button(ref=ref, text="New", icon=ft.icons.CREATE, call_on_click=call_on_click)

    @classmethod
    def edit_button(cls, ref: ft.Ref, call_on_click: Callable, disabled: bool = True):
        btn = cls._button(ref=ref, text="Edit", icon=ft.icons.EDIT_DOCUMENT, call_on_click=call_on_click)
        btn.disabled = disabled

        return btn

    @classmethod
    def delete_button(cls, ref: ft.Ref, call_on_click: Callable, disabled: bool = True):
        btn = cls._button(ref=ref, text="Delete", icon=ft.icons.DELETE, call_on_click=call_on_click)
        btn.disabled = disabled

        return btn

    @classmethod
    def close_button(cls, ref: ft.Ref, call_on_click: Callable):
        return cls._button(ref=ref, text="Close", icon=ft.icons.CLOSE, call_on_click=call_on_click)

    @classmethod
    def datatable(cls, ref: ft.Ref, columns: dict, data: list, call_on_select_changed: Callable):
        cols = [ft.DataColumn(ft.Text(key)) for key in columns.keys()]
        fields = columns.values()
        rows = [ft.DataRow(
            cells=[ft.DataCell(ft.Text(getattr(rec, fld))) for fld in fields],
            on_select_changed=call_on_select_changed
        ) for rec in data]

        return ft.ResponsiveRow(
            controls=[ft.Card(
                content=ft.DataTable(ref=ref, columns=cols, rows=rows),
                col=12)],
            col=12,
            expand=True  # Expands this vertically to take the whole screen
        )

    @classmethod
    def view(cls, controls: list[ft.Control]):
        return ft.View(controls=controls)

    @classmethod
    def _button(cls, ref: ft.Ref, text: str, icon: str, call_on_click: Callable):
        return ft.ElevatedButton(ref=ref, col=1, text=text, icon=icon, on_click=call_on_click)
