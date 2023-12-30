import flet as ft

from contact_app.database import ContactRecord
from flet_mvc.controller import FletMVCController


class ContactsController(FletMVCController):
    def __init__(self):
        super().__init__()

    def contacts_list_select_changed(self, e: ft.ControlEvent):
        selected_id = int(e.control.cells[0].content.value)
        contact = self.model.read(selected_id)

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
        contact = self.model.read(int(self.view.txt_selected_contact.value))
        self.model.delete(contact)

        columns = {"ID": "id", "Firstname": "firstname", "Lastname": "lastname", "Login": "login"}
        fields = columns.values()
        rows = [ft.DataRow(
            cells=[ft.DataCell(ft.Text(getattr(rec, fld))) for fld in fields],
            on_select_changed=self.contacts_list_select_changed
        ) for rec in self.model.all()]

        self.view.tbl_data.rows = rows
        # TODO: this must become a method hiding this complexity

        self.view.btn_edit.text = "Edit"
        self.view.btn_edit.disabled = True
        self.view.btn_delete.text = "Delete"
        self.view.btn_delete.disabled = True

        self.app.refresh()

    def save_new_clicked(self, _: ft.ControlEvent):
        contact = ContactRecord()
        contact = self.view.bind(contact)

        self.model.create(contact)

        self.app.goto("/")

    def cancel_new_clicked(self, _: ft.ControlEvent):
        self.app.goto("/")

    def save_edit_clicked(self, _: ft.ControlEvent):
        contact = self.model.read(int(self.view.txt_id.value))
        contact = self.view.bind(contact)

        self.model.update(contact)

        self.app.goto("/")

    def cancel_edit_clicked(self, _: ft.ControlEvent):
        self.app.goto("/")

