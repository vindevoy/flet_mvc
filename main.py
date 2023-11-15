import flet as ft

from controller import SettingsController
from model import SettingsModel
from mvc import MVCLinker
from view import SettingsView

settings = MVCLinker(SettingsModel, SettingsView, SettingsController)


ft.app(target=settings.build)
