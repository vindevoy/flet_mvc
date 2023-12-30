import flet as ft

from flet_mvc.view import FletMVCView
from flet_mvc.forms import Forms


class ContactsListView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.list_contacts = ft.Ref[ft.DataTable]()
        self.txt_selected_contact = ft.Ref[ft.TextField]()
        self.btn_new = ft.Ref[ft.ElevatedButton]()
        self.btn_edit = ft.Ref[ft.ElevatedButton]()
        self.btn_delete = ft.Ref[ft.ElevatedButton]()
        self.btn_close = ft.Ref[ft.ElevatedButton]()

        self.tbl_data = ft.Ref[ft.DataTable]()

    def build(self) -> ft.View:
        row_title = Forms.title("List of Contacts")

        self.list_contacts, self.tbl_data = Forms.data_table(
            ref=self.list_contacts,
            columns={"ID": "id", "Firstname": "firstname", "Lastname": "lastname", "Login": "login"},
            data=self.model.all(),
            call_on_select_changed=self.controller.contacts_list_select_changed
        )

        self.txt_selected_contact = ft.TextField(ref=self.txt_selected_contact)
        self.txt_selected_contact.visible = False

        self.btn_new = Forms.new_button(ref=self.btn_new, call_on_click=self.controller.button_new_clicked)
        self.btn_edit = Forms.edit_button(ref=self.btn_edit, call_on_click=self.controller.button_edit_clicked)
        self.btn_delete = Forms.delete_button(ref=self.btn_delete, call_on_click=self.controller.button_delete_clicked)
        self.btn_close = Forms.close_button(ref=self.btn_close, call_on_click=self.controller.close_application)

        row_controls = Forms.right_aligned_row(
            controls=[self.btn_new, self.btn_edit, self.btn_delete, self.btn_close])

        return Forms.view([row_title, self.list_contacts, row_controls, self.txt_selected_contact])


class ContactsRecordView(FletMVCView):
    def __init__(self, new_record: bool):
        super().__init__()

        self.new_record = new_record

        self.txt_id = ft.Ref[ft.TextField]()
        self.txt_login = ft.Ref[ft.TextField]()
        self.txt_firstname = ft.Ref[ft.TextField]()
        self.txt_lastname = ft.Ref[ft.TextField]()
        self.txt_email = ft.Ref[ft.TextField]()
        self.txt_address_1 = ft.Ref[ft.TextField]()
        self.txt_address_2 = ft.Ref[ft.TextField]()
        self.txt_postal_code = ft.Ref[ft.TextField]()
        self.txt_city = ft.Ref[ft.TextField]()
        self.txt_country = ft.Ref[ft.TextField]()
        self.txt_phone = ft.Ref[ft.TextField]()
        self.txt_mobile = ft.Ref[ft.TextField]()
        self.txt_fax = ft.Ref[ft.TextField]()

        self.btn_save = ft.Ref[ft.ElevatedButton]()
        self.btn_cancel = ft.Ref[ft.ElevatedButton]()
        self.btn_close = ft.Ref[ft.ElevatedButton]()

    def build(self, contact_id: int = None) -> ft.View:
        if self.new_record:
            row_title = Forms.title(f"New Contact")
        else:
            row_title = Forms.title(f"Edit Contact")

        self.txt_id = ft.TextField(col=3, label="ID", ref=self.txt_id)
        self.txt_id.disabled = True

        self.txt_login = ft.TextField(col=3, label="Login", ref=self.txt_login)
        self.txt_firstname = ft.TextField(col=6, label="Firstname", ref=self.txt_firstname)
        self.txt_lastname = ft.TextField(col=6, label="Lastname", ref=self.txt_lastname)
        self.txt_email = ft.TextField(col=8, label="Email Address", ref=self.txt_email)
        self.txt_address_1 = ft.TextField(col=12, label="Address", ref=self.txt_address_1)
        self.txt_address_2 = ft.TextField(col=12, label="Address (continued)", ref=self.txt_address_2)
        self.txt_postal_code = ft.TextField(col=3, label="Postal Code", ref=self.txt_postal_code)
        self.txt_city = ft.TextField(col=6, label="City", ref=self.txt_city)
        self.txt_country = ft.TextField(col=6, label="Country", ref=self.txt_country)
        self.txt_phone = ft.TextField(col=4, label="Phone", ref=self.txt_phone)
        self.txt_mobile = ft.TextField(col=4, label="Mobile", ref=self.txt_mobile)
        self.txt_fax = ft.TextField(col=4, label="Fax", ref=self.txt_fax)

        if self.new_record:
            id_row = []
        else:
            id_row = [self.txt_id]

        data_form = Forms.data_form(
            rows=[
                id_row,
                [self.txt_login],
                [self.txt_firstname, self.txt_lastname],
                [self.txt_email],
                [self.txt_address_1],
                [self.txt_address_2],
                [self.txt_postal_code, self.txt_city],
                [self.txt_country],
                [self.txt_phone, self.txt_mobile, self.txt_fax]
            ]
        )

        if self.new_record:
            self.btn_save = Forms.save_button(ref=self.btn_save,
                                              call_on_click=self.controller.save_new_clicked)
            self.btn_cancel = Forms.cancel_button(ref=self.btn_cancel,
                                                  call_on_click=self.controller.cancel_new_clicked)
            self.btn_close = Forms.close_button(ref=self.btn_close,
                                                call_on_click=self.controller.close_application)
        else:
            self.btn_save = Forms.save_button(ref=self.btn_save,
                                              call_on_click=self.controller.save_edit_clicked)
            self.btn_cancel = Forms.cancel_button(ref=self.btn_cancel,
                                                  call_on_click=self.controller.cancel_edit_clicked)
            self.btn_close = Forms.close_button(ref=self.btn_close,
                                                call_on_click=self.controller.close_application)

        row_buttons = Forms.right_aligned_row(controls=[self.btn_save, self.btn_cancel, self.btn_close])

        self.fill(contact_id=contact_id)

        return Forms.view(controls=[row_title, data_form, row_buttons])

    def bind(self, contact):
        contact.login = self.txt_login.value  # noqa
        contact.firstname = self.txt_firstname.value  # noqa
        contact.lastname = self.txt_lastname.value  # noqa
        contact.email = self.txt_email.value  # noqa
        contact.address_1 = self.txt_address_1.value  # noqa
        contact.address_2 = self.txt_address_2.value  # noqa
        contact.postal_code = self.txt_postal_code.value  # noqa
        contact.city = self.txt_city.value  # noqa
        contact.country = self.txt_country.value  # noqa
        contact.phone = self.txt_phone.value  # noqa
        contact.mobile = self.txt_mobile.value  # noqa
        contact.fax = self.txt_fax.value  # noqa
        # TODO: fix the warnings above

        return contact

    def fill(self, contact_id):
        if contact_id is None:
            return

        contact = self.model.read(int(contact_id))

        self.txt_id.value = contact.id
        self.txt_login.value = contact.login
        self.txt_firstname.value = contact.firstname
        self.txt_lastname.value = contact.lastname
        self.txt_email.value = contact.email
        self.txt_address_1.value = contact.address_1
        self.txt_address_2.value = contact.address_2
        self.txt_postal_code.value = contact.postal_code
        self.txt_city.value = contact.city
        self.txt_country.value = contact.country
        self.txt_phone.value = contact.phone
        self.txt_mobile.value = contact.mobile
        self.txt_fax.value = contact.fax


class ContactsNewView(ContactsRecordView):
    def __init__(self):
        super().__init__(new_record=True)


class ContactsEditView(ContactsRecordView):
    def __init__(self):
        super().__init__(new_record=False)
