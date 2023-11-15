from mvc import MVCModel


class SettingsModel(MVCModel):
    _genders = {"M": "Male", "F": "Female", "NA": "No answer"}

    @property
    def options(self):
        return list(self._genders.keys())

    def option_name(self, selected_value: str):
        return self._genders[selected_value]
