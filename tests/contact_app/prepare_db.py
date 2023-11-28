from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from contact_app.model import ContactRecord
from database import DatabaseRecord

# create a database in the current directory
current_path = Path(__file__).parent
db_path = current_path.joinpath("contacts.db").absolute()

# remove the database
db_path.unlink(missing_ok=True)

# use pure sqlalchemy to create the database and populate it
engine = create_engine(f"sqlite:///{db_path}")
DatabaseRecord.metadata.create_all(engine)

with Session(engine) as session:
    me = ContactRecord(login="vindevoy",
                       firstname="Yves",
                       lastname="Vindevogel")

    son = ContactRecord(login="nivinog",
                        firstname="Niels",
                        lastname="Vindevogel")

    session.add_all([me, son])
    session.commit()
