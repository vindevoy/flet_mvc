from flet_mvc.component import FletMVCComponent


class FletMVCController(FletMVCComponent):
    def __init__(self):
        """
        Constructor that removes itself from the 3 MVC components as it makes no sense to point to itself.
        """
        super().__init__()

        del self.controller
