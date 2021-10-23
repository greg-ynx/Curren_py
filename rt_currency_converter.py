"""
@Author : lyl_Lynx
@also : This Python script originated from https://data-flair.training/blogs/currency-converter-python/
@Note : I have modified few lines in this script, it is not fully copy/paste
"""

import requests


class RealTimeCurrencyConverter:

    def __init__(self):
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount, n_round=4):
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 28)
        return amount

    def exchange_rate(self, from_currency, to_currency):
        return "Exchnage rate of "+from_currency+" to "+to_currency+" is : "\
               +str(self.currencies[to_currency]/self.currencies[from_currency]*100)+"%"

