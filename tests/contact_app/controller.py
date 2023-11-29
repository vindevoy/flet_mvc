import flet as ft

from flet_mvc.controller import FletMVCController


class ContactsController(FletMVCController):
    def __init__(self):
        super().__init__()

    def contacts_list_select_changed(self, e: ft.ControlEvent):
        selected_id = int(e.control.cells[0].content.value)
        contact = self.model.get_by_id(selected_id)

        self.view.txt_information.value = f"Selected contact: {contact.fullname} #{contact.id}"
        self.view.txt_information.visible = True
        self.view.btn_edit.disabled = False
        self.view.btn_delete.disabled = False

        self.app.refresh()

    def button_new_clicked(self, _: ft.ControlEvent):
        self.app.goto("/new")

    def button_edit_clicked(self, _: ft.ControlEvent):
        contact_id = self.view.txt_information.value.split("#")[1].strip()
        self.app.goto(f"/edit/{contact_id}")

    def button_delete_clicked(self, _: ft.ControlEvent):
        pass

    def close_new_clicked(self, _: ft.ControlEvent):
        self.app.goto("/")

    def close_edit_clicked(self, _: ft.ControlEvent):
        self.app.goto("/")
