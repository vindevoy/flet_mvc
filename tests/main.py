from controller import DemoController
from flet_mvc.app import FletMVCApplication
from model import DemoModel
from view import DemoView

demo_app = FletMVCApplication(model_class=DemoModel,
                                  view_class=DemoView,
                                  controller_class=DemoController)


demo_app.run()
