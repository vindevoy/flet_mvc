# FLET_MVC

## History

Let's start with some history.

I was working with Flet to create a simple application.  This application has:

- one "screen", which is basically one view,
- in that screen, some dropdowns are filled with data from a .yaml config file,
- the user can change the dropdowns and when the user presses "save" another simple file must be written to disk.  Basically, what the user chose in the dropdowns is written in this file.  
 
All very simple.

I wanted to make this in the MVC pattern.  I ran into a problem when I wanted to access my controls in the view from the controller.  I posted this question: https://github.com/flet-dev/flet/discussions/2056

In that question, ndonkoHenri posted that I should have a look at https://github.com/o0Adrian/flet-mvc.  Which I did of course.  However, the DataPoints and the approach in that project is not the way I like things.  Although I have not tried all the stuff in there, it looks a bit overcomplicated to me, especially the approach with those DataPoints.  That's why I started this.  It's another approach on the same problem.

*Note: I am not critisizing that project nor the approach.  It could well be that it is, or will be, better than mine.  I am just taking another approach.  For now as a proof of concept.*

## Purpose

This repo shows an approach towards using the Model-View-Controller pattern in Flet.


## Code and testing

### Conda environment

To run this package, I used a conda environment using the following packages:

- Python
- Flet

### Running

Run the main.py file in the /tests directory.  It will open a desktop Flet application.

## Sample code

### Model

```
class DemoModel(FletMVCModel):
    _genders = {"Male": "M", "Female": "F", "No answer": "NA"}

    def __init__(self):
        super().__init__()

    @property
    def options(self):
        return list(self._genders.keys())

    def option_name(self, selected_value: str):
        return self._genders[selected_value]
```

### View

```
import flet as ft

from flet_mvc.view import FletMVCView


class DemoView(FletMVCView):
    def __init__(self):
        super().__init__()

        self.switch = ft.Ref[ft.Switch]()
        self.dropdown = ft.Ref[ft.Dropdown]()
        self.textfield = ft.Ref[ft.TextField]()
        self.button = ft.Ref[ft.ElevatedButton]()
        self.column = ft.Ref[ft.Column]()

    def build(self, page) -> None:
        super().build(page=page)

        self.switch = ft.Switch(ref=self.switch,
                                label="Dark mode",
                                on_change=self.controller.change_mode)
        self.dropdown = ft.Dropdown(ref=self.dropdown,
                                    options=[ft.dropdown.Option(o) for o in self.model.options],
                                    on_change=self.controller.dropdown_change,
                                    label="Choose gender:")
        self.textfield = ft.TextField(ref=self.textfield,
                                      label="The code for this gender is:",
                                      disabled=True)
        self.button = ft.ElevatedButton(ref=self.button,
                                        text="Close",
                                        on_click=self.controller.button_click)
        self.column = ft.Column(ref=self.column,
                                controls=[self.switch, self.dropdown, self.textfield, self.button])

        self.page.add(self.column)
```

### Controller

```
import flet as ft

from flet_mvc.controller import FletMVCController


class DemoController(FletMVCController):
    def change_mode(self, e: ft.ControlEvent):
        self.view.change_theme_mode(ft.ThemeMode.DARK if e.control.value else ft.ThemeMode.LIGHT)

    def dropdown_change(self, e: ft.ControlEvent = None):  # You must have the ControlEvent as parameter
        self.view.textfield.value = self.model.option_name(self.view.dropdown.value)
        self.update_view()

    def button_click(self, e: ft.ControlEvent = None):
        dlg = ft.AlertDialog(
            modal=True,
            actions=[
                ft.TextButton("Yes", on_click=self.close_application),
                ft.TextButton("No", on_click=self.close_dialog)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            title=ft.Text(f"Close the application ?")
        )

        self.open_dialog(dlg)
```

### Application putting it all together

```
from controller import DemoController
from flet_mvc.app import FletMVCApplication
from model import DemoModel
from view import DemoView

settings_app = FletMVCApplication(model_class=DemoModel,
                                  view_class=DemoView,
                                  controller_class=DemoController)


settings_app.run()
```




