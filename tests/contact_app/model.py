from pathlib import Path

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from flet_mvc.model import FletMVCModel, Base


class ContactsModel(FletMVCModel):
    def __init__(self):
        super().__init__()

    def get_all(self):
        return super()._get_all(Contact)

    def get_by_id(self, item_id):
        return super()._get_by_id(Contact, item_id)


class Contact(Base):
    __tablename__ = "contact"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(30))
    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(70))

    def __repr__(self) -> str:
        return f"Contact(id={self.id}, login={self.login}, fullname={self.lastname.upper()}, {self.firstname})"


if __name__ == "__main__":
    current_path = Path(__file__).parent
    db_path = current_path.joinpath("contacts.db").absolute()

    contacts = ContactsModel()
    contacts.bind_database(f"sqlite:///{db_path}")

    assert len(contacts.get_all()) == 2

    me = contacts.get_by_id(1)

    assert me.id == 1
    assert me.firstname == "Yves"
    assert me.lastname == "Vindevogel"
    assert me.login == "vindevoy"
