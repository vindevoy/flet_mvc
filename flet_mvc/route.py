from module import FletMVCModule


class FletMVCRoute:
    def __init__(self, path: str, module: FletMVCModule):
        self.path: str = path
        self.module = module

    def is_dynamic(self):
        return "/:" in self.path
