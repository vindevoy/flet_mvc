from sqlalchemy.orm import DeclarativeBase


class DatabaseRecord(DeclarativeBase):
    def __int__(self):
        super().__init__()
