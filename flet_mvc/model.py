from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class FletMVCModel:
    def __init__(self, record_type):  # TODO: add hinting
        """
        Constructor to set the parent app which will be filled out when the MVC module is added to the app.
        It also sets the 2 other components in the MVC pattern.  That will be filled out when the 3 are combined
        in the MVC module's constructor.
        """
        self.app = None
        self.view = None
        self.controller = None

        self.__record_type = record_type

        self.__connection_string = ""

    def bind_database(self, connection_string: str):
        self.__connection_string = connection_string

    def get_all(self):
        with self._get_session() as session:
            return session.query(self.__record_type).all()

    def get_by_id(self, item_id: int):
        with self._get_session() as session:
            return session.get(self.__record_type, item_id)

    def add_record(self, record):
        with self._get_session() as session:
            session.add(record)
            session.commit()

    def _get_session(self):
        engine = create_engine(self.__connection_string, echo=True)
        maker = sessionmaker(bind=engine)
        session = maker()

        return session
