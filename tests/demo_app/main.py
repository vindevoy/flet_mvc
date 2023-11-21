from demo_app.controller import DemoController
from demo_app.model import DemoModel
from demo_app.view import DemoView
from flet_mvc.app import FletMVCApplication
from module import FletMVCModule

app = FletMVCApplication("Simple demo app")

settings_module = FletMVCModule(model_class=DemoModel, view_class=DemoView, controller_class=DemoController)


app.add_route("/", settings_module)
app.run()
