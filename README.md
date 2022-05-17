# GUI WITH PySimpleGUI LIBRARY
Projects in the repository use [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) library to implement several GUI examples as presented in [Clear Code's excellent intro to PySimpleGUI](https://www.youtube.com/watch?v=QeMaWQZllhg).

> We note that these examples are references for neither best programming practices nor good design. Their purpose is only to introduce the PySimpleGUI for developing desktop apps with Python.

## Overview of Projects
Each folder groups a single example as follows:

- [_converter_](./converter/) is the simplest implementation. This project introduces basic components, such as Window, Text and Button. In addition, it shows how to put all these together to make a simple desktop app.

- [_calculator_](./calculator/) introduces theming support, contextual menu and styling. A calculator is implemented to show case.

- [_stopwatch_](./stopwatch/) shows further styling features by implementing a stopwatch.

- [_text-editor_](./text-editor/) implements a simple text editor that enables saving and loading content. It main feature is to show how to create window menus.

## Dependencies
Each project may have additional dependencies. However, as all projects use PySimpleGUI, this is the primary depedency. One can get the dependency by running: `python3 -m pip install PySimpleGUI`.

In addition, as PySimpleGUI uses [TKinter](https://realpython.com/python-gui-tkinter/) under the hood, this is also an essential dependency. If you are using a Mac,  you can install it using [Homebrew](https://brew.sh) package manager: `brew install python-tk`
