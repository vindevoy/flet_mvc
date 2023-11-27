from pathlib import Path

from app import FletMVCApplication
from contact_app.controller import ContactsController
from contact_app.model import ContactsModel
from contact_app.view import ContactsView
from module import FletMVCModule

current_path = Path(__file__).parent
db_path = current_path.joinpath("contacts.db").absolute()

app = FletMVCApplication("Contact MVC")
app.bind_database(f"sqlite:///{db_path}")

contacts = FletMVCModule(model_class=ContactsModel,
                         view_class=ContactsView,
                         controller_class=ContactsController)

app.add_route("/", contacts)

app.run()
