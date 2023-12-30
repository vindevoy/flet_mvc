import flet as ft

from contact_app.database import ContactRecord
from flet_mvc.controller import FletMVCController


class ContactsController(FletMVCController):
    def __init__(self):
        super().__init__()

    def contacts_list_select_changed(self, e: ft.ControlEvent):
        selected_id = int(e.control.cells[0].content.value)
        contact = self.model.get_by_id(selected_id)

        self.view.txt_selected_contact.value = str(contact.id)
        self.view.btn_edit.text = f"Edit #{selected_id}"
        self.view.btn_edit.disabled = False
        self.view.btn_delete.text = f"Delete #{selected_id}"
        self.view.btn_delete.disabled = False

        self.app.refresh()

    def button_new_clicked(self, e: ft.ControlEvent):
        self.app.goto("/new")

    def button_edit_clicked(self, _: ft.ControlEvent):
        contact_id = int(self.view.txt_selected_contact.value.strip())
        self.app.goto(f"/edit/{contact_id}")

    def button_delete_clicked(self, _: ft.ControlEvent):
        pass

    def save_new_clicked(self, _: ft.ControlEvent):
        contact = ContactRecord(
            login = self.view.txt_login.value,
            firstname = self.view.txt_firstname.value,
            lastname = self.view.txt_lastname.value,
            email = self.view.txt_email.value,
            address_1 = self.view.txt_address_1.value,
            address_2 = self.view.txt_address_2.value,
            postal_code = self.view.txt_postal_code.value,
            city = self.view.txt_city.value,
            country = self.view.txt_country.value,
            phone = self.view.txt_phone.value,
            mobile = self.view.txt_mobile.value,
            fax = self.view.txt_fax.value)

        self.model.add_record(contact)

    def cancel_new_clicked(self, _: ft.ControlEvent):
        self.app.goto("/")

    def save_edit_clicked(self, _: ft.ControlEvent):
        pass

    def cancel_edit_clicked(self, _: ft.ControlEvent):
        self.app.goto("/")

