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




