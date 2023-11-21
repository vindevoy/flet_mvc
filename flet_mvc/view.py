class FletMVCView:
    def __init__(self):
        """
        Constructor that creates the 2 other components in the MVC pattern and the parent application.
        They will be set by the FletMVCModule.
        """
        self.app = None
        self.model = None
        self.controller = None
