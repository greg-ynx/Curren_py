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
from kivy.config import Config

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '800')
Builder.load_file('main_window.kv')


class MainFrame(Widget):

    def __init__(self):
        super().__init__()
        self.currency_converter = CurrencyConverter()
        with open(os.path.join(data_dir, 'currencyNames.json'), 'r', encoding='utf8') as f:
            data = json.load(f)
        self.data = data
        self.currency_list = [data[key]['name'] for key in data]
        self.ids.c1_spinner.values = self.ids.c2_spinner.values = self.currency_list
        self.ids.c1_spinner.text = self.ids.c2_spinner.text = data['USD']['name']
        self.ids.c1_text_input.bind(on_text_validate=self.refresh_values)
        self.ids.c2_text_input.bind(on_text_validate=self.refresh_values)

    def exchange(self, kv_id, from_currency, to_currency):
        from_key = 'USD'
        to_key = 'USD'
        for key in self.data:
            if self.data[key]['name'] == from_currency:
                from_key = key
            if self.data[key]['name'] == to_currency:
                to_key = key
        if kv_id == self.ids.c1_spinner:
            self.ids.c2_text_input.text = str(self.currency_converter.convert(
                from_key,
                to_key,
                float(self.ids.c1_text_input.text)
            ))
            from_value = float(self.ids.c2_text_input.text)
            to_value = float(self.ids.c1_text_input.text)
        else:
            self.ids.c1_text_input.text = str(self.currency_converter.convert(
                from_key,
                to_key,
                float(self.ids.c2_text_input.text)
            ))
            from_value = float(self.ids.c1_text_input.text)
            to_value = float(self.ids.c2_text_input.text)
        self.ids.exchange_rate_label.text = f"Exchange rate \n" \
                                            f"from {from_key} to {to_key} is : " \
                                            f"{int(to_value / from_value)}%"

    def get_key_from_value(self, value: str):
        keys = [k for k in self.data if self.data[k]['name'] == value]
        if keys:
            return keys[0]
        return None

    def refresh_values(self, instance):
        if instance.ids == self.ids.c1_text_input:
            self.ids.c2_text_input.text = str(self.currency_converter.convert(
                self.get_key_from_value(self.ids.c2_spinner.text),
                self.get_key_from_value(self.ids.c1_spinner.text),
                float(self.ids.c1_text_input.text)
            ))
        else:
            self.ids.c1_text_input.text = str(self.currency_converter.convert(
                self.get_key_from_value(self.ids.c1_spinner.text),
                self.get_key_from_value(self.ids.c2_spinner.text),
                float(self.ids.c2_text_input.text)
            ))


class Curren_pyApp(App):

    def build(self):
        self.icon = os.path.join(img_dir, 'curren_py_logo.png')
        return MainFrame()


if __name__ == "__main__":
    Curren_pyApp().run()
