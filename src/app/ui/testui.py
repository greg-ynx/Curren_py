import os
from config.definitions import data_dir
import json
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from src.app.CurrencyConverter.CurrencyConverter import CurrencyConverter


class MyGridLayout(GridLayout):

    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.currency_converter = CurrencyConverter()

        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # left currency amount text input
        self.currency_1_label = Label(text="Currency 1 :")
        self.top_grid.add_widget(self.currency_1_label)
        self.currency_1_text_input = TextInput(multiline=False)
        self.top_grid.add_widget(self.currency_1_text_input)

        # right currency amount text input
        self.currency_2_label = Label(text="Currency 2 :")
        self.top_grid.add_widget(self.currency_2_label)
        self.currency_2_text_input = TextInput(multiline=False)
        self.top_grid.add_widget(self.currency_2_text_input)

        self.add_widget(self.top_grid)

        # Test conversion Button
        self.convert_button = Button(text="Conversion", font_size=11)
        self.convert_button.bind(on_press=self.conversion_test)
        self.add_widget(self.convert_button)

    def conversion_test(self, instance):
        res = self.currency_converter.convert("USD", "EUR", float(self.currency_1_text_input.text))
        self.currency_2_text_input.text = str(res)


class MyApp(App):

    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
