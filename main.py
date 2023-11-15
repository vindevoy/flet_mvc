import flet as ft

from controller import SettingsController
from model import SettingsModel
from mvc import MVCPattern
from view import SettingsView


pattern = MVCPattern(SettingsModel, SettingsView, SettingsController)
view = pattern.view


ft.app(target=view.build)
