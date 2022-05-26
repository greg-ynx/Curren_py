import os
import re
from config.definitions import data_dir, img_dir
import json
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
# noinspection PyUnresolvedReferences
from kivy.properties import ObjectProperty
from src.app.CurrencyConverter.CurrencyConverter import CurrencyConverter
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '800')
Builder.load_file('main_window.kv')


class MainFrame(Widget):

    def __init__(self, **kwargs):
        super(MainFrame, self).__init__(**kwargs)
        self.currency_converter = CurrencyConverter()
        with open(os.path.join(data_dir, 'currencyNames.json'), 'r', encoding='utf8') as f:
            data = json.load(f)
        self.data = data
        self.currency_list = [data[key]['name'] for key in data]
        print(self.currency_list)
        self.ids.c1_spinner.values = self.ids.c2_spinner.values = self.currency_list
        self.ids.c1_spinner.text = self.ids.c2_spinner.text = data['USD']['name']
        self.ids.c1_spinner.bind(text=self.change_spinner)
        self.ids.c2_spinner.bind(text=self.change_spinner)
        self.ids.c1_text_input.bind(focus=self.refresh_values)
        self.ids.c2_text_input.bind(focus=self.refresh_values)

    def get_key_from_value(self, value: str):
        keys = [key for key in self.data if self.data[key]['name'] == value]
        if keys:
            print(keys)
            return keys[0]
        return None

    def change_spinner(self, spinner, text):
        from_key = self.get_key_from_value(text)
        if spinner == self.ids.c1_spinner:
            to_key = self.get_key_from_value(self.ids.c2_spinner.text)
            self.ids.c2_text_input.text = str(self.currency_converter.convert(
                from_key,
                to_key,
                float(self.ids.c1_text_input.text)
            ))
        else:
            to_key = self.get_key_from_value(self.ids.c1_spinner.text)
            self.ids.c1_text_input.text = str(self.currency_converter.convert(
                from_key,
                to_key,
                float(self.ids.c2_text_input.text)
            ))
        self.ids.exchange_rate_label.text = f"Exchange rate \n" \
                                            f"from {from_key} to {to_key} is : " \
                                            f"{round(self.currency_converter.get_rate(from_key, to_key), 4)}"

    def refresh_values(self, instance, value):
        if value == '':
            instance.text = str(.0)
        if instance == self.ids.c1_text_input:
            self.ids.c2_text_input.text = str(self.currency_converter.convert(
                self.get_key_from_value(self.ids.c1_spinner.text),
                self.get_key_from_value(self.ids.c2_spinner.text),
                float(self.ids.c1_text_input.text)
            ))
        else:
            self.ids.c1_text_input.text = str(self.currency_converter.convert(
                self.get_key_from_value(self.ids.c2_spinner.text),
                self.get_key_from_value(self.ids.c1_spinner.text),
                float(self.ids.c2_text_input.text)
            ))


class Curren_pyApp(App):

    def build(self):
        self.icon = os.path.join(img_dir, 'curren_py_logo.png')
        return MainFrame()


if __name__ == "__main__":
    Curren_pyApp().run()
