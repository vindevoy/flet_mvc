from pathlib import Path

from contact_app.database import ContactRecord
from flet_mvc.model import FletMVCModel


class ContactsModel(FletMVCModel):
    def __init__(self):
        super().__init__(record_type=ContactRecord)


if __name__ == "__main__":
    current_path = Path(__file__).parent
    db_path = current_path.joinpath("contacts.db").absolute()

    contacts = ContactsModel()
    contacts.bind_database(f"sqlite:///{db_path}")

    assert len(contacts.all()) > 0

    me = contacts.read(1)

    assert me.id == 1
    assert me.firstname == "Yves"
    assert me.lastname == "Vindevogel"
    assert me.login == "vindevoy"
