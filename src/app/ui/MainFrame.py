import os
from config.definitions import data_dir, img_dir
import json
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
# noinspection PyUnresolvedReferences
from kivy.properties import ObjectProperty
from src.app.CurrencyConverter.CurrencyConverter import CurrencyConverter
from kivy.lang import Builder


Builder.load_file('main_window.kv')


class MainFrame(Widget):

    currency_1 = ObjectProperty(None)
    currency_2 = ObjectProperty(None)
    currency_converter = CurrencyConverter()

    def conversion_test(self):
        res = self.currency_converter.convert("USD", "EUR", float(self.currency_1_text_input.text))
        self.currency_2_text_input.text = str(res)


class Curren_pyApp(App):

    def build(self):
        self.icon = os.path.join(img_dir, 'curren_py_logo.png')
        return MainFrame()


if __name__ == "__main__":
    Curren_pyApp().run()
