import flet as ft

from flet_mvc.controller import FletMVCController


class ContactsController(FletMVCController):
    def __init__(self):
        super().__init__()

    def contacts_list_select_changed(self, e: ft.ControlEvent):
        selected_id = int(e.control.cells[0].content.value)
        contact = self.model.get_by_id(selected_id)

        self.view.txt_selected_contact.value = f"Selected contact: {contact.fullname} #{contact.id}"
        self.view.txt_selected_contact.update()

    def button_new_clicked(self, e: ft.ControlEvent):
        pass

    def button_edit_clicked(self, e: ft.ControlEvent):
        pass

    def button_delete_clicked(self, e: ft.ControlEvent):
        pass
