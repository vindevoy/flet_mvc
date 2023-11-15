from flet_mvc.model import FletMVCModel


class DemoModel(FletMVCModel):
    _genders = {"M": "Male", "F": "Female", "NA": "No answer"}

    def __init__(self):
        super().__init__()

    @property
    def options(self):
        return list(self._genders.keys())

    def option_name(self, selected_value: str):
        return self._genders[selected_value]
