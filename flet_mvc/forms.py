from typing import Callable

import flet as ft


class Forms:
    @classmethod
    def title(cls, title: str, ref: ft.Ref = None):
        title_size = 28
        title_color = ft.colors.BLUE_900

        icon = ft.Icon(ft.icons.CONTACT_PAGE, size=title_size, color=title_color)
        txt_title = ft.Text(title, size=title_size, weight=ft.FontWeight.W_600, color=title_color)

        return ft.Row(controls=[icon, txt_title], col=12, ref=ref)

    @classmethod
    def left_aligned_row(cls, controls: list[ft.Control], ref: ft.Ref = None):
        return ft.Row(controls=controls, alignment=ft.MainAxisAlignment.START, ref=ref, col=12)

    @classmethod
    def center_aligned_row(cls, controls: list[ft.Control], ref: ft.Ref = None):
        return ft.Row(controls=controls, alignment=ft.MainAxisAlignment.CENTER, ref=ref, col=12)

    @classmethod
    def right_aligned_row(cls, controls: list[ft.Control], ref: ft.Ref = None):
        return ft.Row(controls=controls, alignment=ft.MainAxisAlignment.END, ref=ref, col=12)

    @classmethod
    def new_button(cls, call_on_click: Callable, ref: ft.Ref = None):
        return cls._button(ref=ref, text="New", icon=ft.icons.CREATE, call_on_click=call_on_click)

    @classmethod
    def edit_button(cls, call_on_click: Callable, disabled: bool = True, ref: ft.Ref = None):
        btn = cls._button(ref=ref, text="Edit", icon=ft.icons.EDIT_DOCUMENT, call_on_click=call_on_click)
        btn.disabled = disabled

        return btn

    @classmethod
    def save_button(cls, call_on_click: Callable, ref: ft.Ref = None):
        return cls._button(ref=ref, text="Save", icon=ft.icons.SAVE, call_on_click=call_on_click)

    @classmethod
    def cancel_button(cls, call_on_click: Callable, ref: ft.Ref = None):
        return cls._button(ref=ref, text="Cancel", icon=ft.icons.CANCEL, call_on_click=call_on_click)

    @classmethod
    def delete_button(cls, call_on_click: Callable, disabled: bool = True, ref: ft.Ref = None):
        btn = cls._button(ref=ref, text="Delete", icon=ft.icons.DELETE, call_on_click=call_on_click)
        btn.disabled = disabled

        return btn

    @classmethod
    def close_button(cls, call_on_click: Callable, ref: ft.Ref = None):
        return cls._button(ref=ref, text="Close", icon=ft.icons.DOOR_FRONT_DOOR, call_on_click=call_on_click)

    @classmethod
    def data_table(cls, columns: dict, data: list, call_on_select_changed: Callable, ref: ft.Ref = None):
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
    def data_form(cls, rows: list[list[ft.Control]], ref: ft.Ref = None):
        form_rows = [ft.ResponsiveRow(controls=row) for row in rows if len(row) > 0]

        return ft.ResponsiveRow(
            controls=[ft.Card(
                content=ft.Container(
                    content=ft.Column(controls=form_rows),
                    margin=12
                )
            )],
            col=12,
            ref=ref,
            expand=True  # Expands this vertically to take the whole screen
        )

    @classmethod
    def view(cls, controls: list[ft.Control]):
        return ft.View(controls=controls)

    @classmethod
    def _button(cls, text: str, icon: str, call_on_click: Callable, ref: ft.Ref = None):
        return ft.ElevatedButton(ref=ref, text=text, icon=icon, on_click=call_on_click, width=140)
