from flet_mvc.controller import FletMVCController
from flet_mvc.model import FletMVCModel
from flet_mvc.view import FletMVCView


class FletMVCApplication:
    def __init__(self,
                 model_class: FletMVCModel.__class__,
                 view_class: FletMVCView.__class__,
                 controller_class: FletMVCController.__class__):
        """
        This class links the 3 parts of an MVC application together

        :param model_class: the FletMVCModel class name (no instance!)
        :param view_class: the FletMVCView class name (no instance!)
        :param controller_class: the FletMVCController class name (no instance!)
        """
        # Instantiate the classes.  You must pass the class, not an instance !
        self.model = model_class()
        self.view = view_class()
        self.controller = controller_class()

        # Update the model to make controller and view accessible
        self.model.view = self.view
        self.model.controller = self.controller

        # Update the view to make the model and controller accessible
        self.view.model = self.model
        self.view.controller = self.controller

        # Update the controller to make the model and view accessible
        self.controller.model = self.model
        self.controller.view = self.view

    def build(self, page) -> None:
        """
        Convenience method that passes the build to the view

        :param page: ft.Page: the page that is passed via ft.app(target=page).
        You need to set this method as the target parameter.
        The method will be called passing the page parameter.  The page is the Flet page that needs to be built.
        """
        self.view.build(page)
