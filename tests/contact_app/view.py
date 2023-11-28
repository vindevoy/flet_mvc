import flet as ft

from flet_mvc.controls import Controls
from flet_mvc.view import FletMVCView


class ContactsListView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.list_contacts = ft.Ref[ft.DataTable]()
        self.txt_selected_contact = ft.Ref[ft.TextField]()
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
        self.btn_close = ft.ElevatedButton(ref=self.btn_close, col=2, text="Close",
                                           on_click=self.controller.close_application)
        self.view = ft.View(controls=[self.list_contacts, self.txt_selected_contact, self.btn_close])

        return self.view
