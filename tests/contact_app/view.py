import flet as ft

from flet_mvc.view import FletMVCView
from flet_mvc.forms import Forms


class ContactsListView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.list_contacts = ft.Ref[ft.DataTable]()
        self.txt_information = ft.Ref[ft.TextField]()
        self.btn_new = ft.Ref[ft.ElevatedButton]()
        self.btn_edit = ft.Ref[ft.ElevatedButton]()
        self.btn_delete = ft.Ref[ft.ElevatedButton]()
        self.btn_close = ft.Ref[ft.ElevatedButton]()

    def build(self) -> ft.View:
        row_title = Forms.title("List of Contacts")

        self.list_contacts = Forms.datatable(
            ref=self.list_contacts,
            columns={"ID": "id", "Firstname": "firstname", "Lastname": "lastname", "Login": "login"},
            data=self.model.get_all(),
            call_on_select_changed=self.controller.contacts_list_select_changed
        )

        self.txt_information = Forms.information_text(ref=self.txt_information)

        self.btn_new = Forms.new_button(ref=self.btn_new, call_on_click=self.controller.button_new_clicked)
        self.btn_edit = Forms.edit_button(ref=self.btn_edit, call_on_click=self.controller.button_edit_clicked)
        self.btn_delete = Forms.delete_button(ref=self.btn_delete, call_on_click=self.controller.button_delete_clicked)
        self.btn_close = Forms.close_button(ref=self.btn_close, call_on_click=self.controller.close_application)

        row_controls = Forms.right_aligned_row(controls=[self.txt_information, self.btn_new, self.btn_edit,
                                                         self.btn_delete, self.btn_close])

        return Forms.view([row_title, self.list_contacts, row_controls])


class ContactsNewView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.btn_close = ft.Ref[ft.ElevatedButton]()

    def build(self) -> ft.View:
        row_title = Forms.title(f"New Contact")

        self.btn_close = Forms.close_button(ref=self.btn_close, call_on_click=self.controller.close_new_clicked)
        row_buttons = Forms.right_aligned_row(controls=[self.btn_close])

        return Forms.view(controls=[row_title, row_buttons])


class ContactsEditView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.btn_close = ft.Ref[ft.ElevatedButton]()

    def build(self, contact_id: str) -> ft.View:
        contact = self.model.get_by_id(int(contact_id))

        row_title = Forms.title(f"Edit Contact: {contact.fullname}")

        self.btn_close = Forms.close_button(ref=self.btn_close, call_on_click=self.controller.close_edit_clicked)
        row_buttons = Forms.right_aligned_row(controls=[self.btn_close])

        return Forms.view(controls=[row_title, row_buttons])
