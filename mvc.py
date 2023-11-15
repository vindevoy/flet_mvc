import flet as ft
from flet_core.connection import Connection


class MVCModel:
    def __init__(self):
        self.controller = None
        self.view = None


class MVCView:
    def __init__(self):
        self.model = None
        self.controller = None

        self.page = None


class MVCController:
    def __init__(self):
        self.model = None
        self.view = None


class MVCPattern:
    def __init__(self, model_class, view_class, controller_class):
        self.model = model_class()
        self.view = view_class()
        self.controller = controller_class()

        self.model.controller = self.controller
        self.model.view = self.view

        self.view.model = self.model
        self.view.controller = self.controller

        self.controller.model = self.model
        self.controller.view = self.view
