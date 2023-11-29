from pathlib import Path

from app import FletMVCApplication
from contact_app.controller import ContactsController
from contact_app.model import ContactsModel
from contact_app.view import ContactsListView, ContactsEditView, ContactsNewView
from module import FletMVCModule

current_path = Path(__file__).parent
db_path = current_path.joinpath("contacts.db").absolute()

app = FletMVCApplication("Contact MVC")
app.bind_database(f"sqlite:///{db_path}")

contact_list = FletMVCModule(model_class=ContactsModel,
                             view_class=ContactsListView,
                             controller_class=ContactsController)

contact_new = FletMVCModule(model_class=ContactsModel,
                            view_class=ContactsNewView,
                            controller_class=ContactsController)

contact_edit = FletMVCModule(model_class=ContactsModel,
                             view_class=ContactsEditView,
                             controller_class=ContactsController)

app.add_route("/", contact_list)
app.add_route("/new", contact_new)
app.add_route("/edit/:contact_id", contact_edit)

app.run()
