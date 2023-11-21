class FletMVCModel:
    def __init__(self):
        """
        Constructor that creates the 2 other components in the MVC pattern.  They will be set by the FletMVCApp.
        """
        self.app = None
        self.controller = None
        self.view = None
