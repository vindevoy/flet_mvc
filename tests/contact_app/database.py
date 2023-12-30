from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from db import DatabaseRecord


class ContactRecord(DatabaseRecord):
    __tablename__ = "contacts"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(30))
    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(70))
    email: Mapped[str] = mapped_column(String(250))
    address_1: Mapped[str] = mapped_column(String(250))
    address_2: Mapped[str] = mapped_column(String(250))
    postal_code: Mapped[str] = mapped_column(String(15))
    city: Mapped[str] = mapped_column(String(200))
    country: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(30))
    mobile: Mapped[str] = mapped_column(String(30))
    fax: Mapped[str] = mapped_column(String(30))

    @property
    def fullname(self):
        return f"{self.lastname.strip().upper()}, {self.firstname} "

    def __repr__(self) -> str:
        return f"Contact(id={self.id}, login={self.login}, fullname={self.fullname})"
