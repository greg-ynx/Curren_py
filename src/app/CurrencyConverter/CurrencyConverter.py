# This script is made by greg.ynx
#
# Attribution to Exchange Rate API https://www.exchangerate-api.com for the rates

import requests


class CurrencyConverter:

    def __init__(self):
        url = "https://open.er-api.com/v6/latest/USD"
        self.data, self.rates = self.refresh_rates(url)

    def convert(self, from_currency, to_currency, amount):
        print(from_currency, to_currency, amount)
        if from_currency != 'USD':
            amount /= self.rates[from_currency]
        return round(amount * self.rates[to_currency], 4)

    def get_rate(self, from_currency, to_currency):
        return 1 / self.rates[from_currency] * self.rates[to_currency]

    @staticmethod
    def refresh_rates(url):
        data = requests.get(url).json()
        rates = data['rates']
        return data, rates
