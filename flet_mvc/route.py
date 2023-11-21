from module import FletMVCModule


class FletMVCRoute:
    def __init__(self, path: str, module: FletMVCModule):
        """
        Constructor for keeping the path and the module parameters.
        """
        self.path: str = path
        self.module = module

    def is_dynamic(self) -> bool:
        """
        Returns whether a route is dynamic or not.  A dynamic route is when there are parameters passed.
        Parameters are passed with the ":param_name" notation.

        :return: bool
        """
        return "/:" in self.path
