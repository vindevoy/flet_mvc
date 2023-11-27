from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    def __int__(self):
        super().__init__()


class FletMVCModel:
    def __init__(self):
        """
        Constructor to set the parent app which will be filled out when the MVC module is added to the app.
        It also sets the 2 other components in the MVC pattern.  That will be filled out when the 3 are combined
        in the MVC module's constructor.
        """
        self.app = None
        self.view = None
        self.controller = None

        self.__connection_string = ""

    def bind_database(self, connection_string: str):
        self.__connection_string = connection_string

    def _get_all(self, database_class):
        with self._get_session() as session:
            return session.query(database_class).all()

    def _get_by_id(self, database_class, item_id: int):
        with self._get_session() as session:
            return session.get(database_class, item_id)

    def _get_session(self):
        engine = create_engine(self.__connection_string, echo=True)
        maker = sessionmaker(bind=engine)
        session = maker()

        return session
