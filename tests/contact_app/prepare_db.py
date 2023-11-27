from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from contact_app.model import Contact
from model import Base

# create a database in the current directory
current_path = Path(__file__).parent
db_path = current_path.joinpath("contacts.db").absolute()

# remove the database
db_path.unlink(missing_ok=True)

# use pure sqlalchemy to create the database and populate it
engine = create_engine(f"sqlite:///{db_path}")
Base.metadata.create_all(engine)

with Session(engine) as session:
    me = Contact(login="vindevoy",
                 firstname="Yves",
                 lastname="Vindevogel")

    son = Contact(login="nivinog",
                  firstname="Niels",
                  lastname="Vindevogel")

    session.add_all([me, son])
    session.commit()
