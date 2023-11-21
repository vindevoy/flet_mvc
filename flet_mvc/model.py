class FletMVCModel:
    def __init__(self):
        """
        Constructor to set the parent app which will be filled out when the MVC module is added to the app.
        It also sets the 2 other components in the MVC pattern.  That will be filled out when the 3 are combined
        in the MVC module's constructor.
        """
        self.app = None
        self.view = None
        self.controller = None
