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
        self.cols = 2
        self.currency_converter = CurrencyConverter()
        with open(os.path.join(data_dir, 'currencyNames.json'), encoding='utf-8') as f:
            d = json.load(f)
        self.currencies = [key for key in d]

        # left currency select component
        self.currency_1_drop_down = DropDown()
        for key in d:
            btn = Button(text=key)
            btn.bind(on_press=lambda btn: self.currency_1_drop_down.select(btn.text))
            self.currency_1_drop_down.add_widget(btn)
        self.add_widget(self.currency_1_drop_down)

        # right currency select component
        self.currency_2_drop_down = DropDown()
        for key in d:
            btn = Button(text=key)
            btn.bind(on_press=lambda btn: self.currency_2_drop_down.select(btn.text))
            self.currency_2_drop_down.add_widget(btn)
        self.add_widget(self.currency_2_drop_down)

        # left currency amount text input
        self.currency_1_text_input = TextInput(multiline=False)
        self.add_widget(self.currency_1_text_input)

        # right currency amount text input
        self.currency_2_text_input = TextInput(multiline=False)
        self.add_widget(self.currency_2_text_input)

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
