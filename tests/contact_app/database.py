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

    @property
    def fullname(self):
        return f"{self.lastname.strip().upper()}, {self.firstname} "

    def __repr__(self) -> str:
        return f"Contact(id={self.id}, login={self.login}, fullname={self.fullname})"
