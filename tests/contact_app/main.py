from app import FletMVCApplication
from contact_app.controller import ContactsController
from contact_app.model import ContactsModel
from contact_app.view import ContactsView
from module import FletMVCModule

app = FletMVCApplication("Contact MVC")

contacts = FletMVCModule(model_class=ContactsModel,
                         view_class=ContactsView,
                         controller_class=ContactsController)

app.add_route("/", contacts)

app.bind_database("sqlite://")
app.run()
