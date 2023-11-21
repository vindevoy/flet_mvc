# from flet_mvc.model import FletMVCModel
#
#
# class DemoModel(FletMVCModel):
#     _genders = {"Male": "M", "Female": "F", "No answer": "NA"}
#
#     def __init__(self):
#         super().__init__()
#
#     @property
#     def options(self):
#         return list(self._genders.keys())
#
#     def option_code(self, selected_value: str):
#         return self._genders[selected_value]
