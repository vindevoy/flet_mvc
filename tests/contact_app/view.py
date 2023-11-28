import flet as ft

from flet_mvc.controls import Controls
from flet_mvc.view import FletMVCView


class ContactsListView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.list_contacts = ft.Ref[ft.DataTable]()
        self.txt_selected_contact = ft.Ref[ft.TextField]()
        self.btn_new = ft.Ref[ft.ElevatedButton]()
        self.btn_edit = ft.Ref[ft.ElevatedButton]()
        self.btn_delete = ft.Ref[ft.ElevatedButton]()
        self.btn_close = ft.Ref[ft.ElevatedButton]()
        self.view = ft.Ref[ft.View]()

    def build(self) -> ft.View:
        self.list_contacts = Controls.build_datatable(
            ref=self.list_contacts,
            columns={"ID": "id", "Firstname": "firstname", "Lastname": "lastname", "Login": "login"},
            data=self.model.get_all(),
            on_select_changed=self.controller.contacts_list_select_changed
        )
        self.txt_selected_contact = ft.TextField(ref=self.txt_selected_contact, disabled=True, value="")

        self.btn_new = ft.ElevatedButton(ref=self.btn_close, col=2, text="New", icon=ft.icons.CREATE,
                                         on_click=self.controller.button_new_clicked)
        self.btn_edit = ft.ElevatedButton(ref=self.btn_close, col=2, text="Edit", icon=ft.icons.EDIT_DOCUMENT,
                                          on_click=self.controller.button_edit_clicked)
        self.btn_delete = ft.ElevatedButton(ref=self.btn_close, col=2, text="Delete", icon=ft.icons.DELETE,
                                            on_click=self.controller.button_delete_clicked)
        self.btn_close = ft.ElevatedButton(ref=self.btn_close, col=2, text="Close", icon=ft.icons.CLOSE,
                                           on_click=self.controller.close_application)
        row_buttons = ft.Row(controls=[self.btn_new, self.btn_edit, self.btn_delete, self.btn_close])

        self.view = ft.View(controls=[self.list_contacts, self.txt_selected_contact, row_buttons])

        return self.view
