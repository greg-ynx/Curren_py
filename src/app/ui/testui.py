import os
from config.definitions import data_dir
import json
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
import kivy.properties as kyprops
from src.app.CurrencyConverter.CurrencyConverter import CurrencyConverter


class MyGridLayout(Widget):

    currency_1 = kyprops.ObjectProperty(None)
    currency_2 = kyprops.ObjectProperty(None)
    currency_converter = CurrencyConverter()

    def press(self):
        print(self.currency_1.text)

    def conversion_test(self):
        res = self.currency_converter.convert("USD", "EUR", float(self.currency_1_text_input.text))
        self.currency_2_text_input.text = str(res)



class MyApp(App):

    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
