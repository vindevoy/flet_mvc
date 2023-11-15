from controller import DemoController
from flet_mvc.app import FletMVCApplication
from model import DemoModel
from view import DemoView

settings_app = FletMVCApplication(model_class=DemoModel,
                                  view_class=DemoView,
                                  controller_class=DemoController)


settings_app.run()
