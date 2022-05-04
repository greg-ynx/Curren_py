# This script is made by greg.ynx
#
# Attribution to Exchange Rate API https://www.exchangerate-api.com for the rates

import requests


class CurrencyConverter:

    def __init__(self):
        url = "https://open.er-api.com/v6/latest/USD"
        self.data, self.rates = self.refresh_rates(url)
        print(self.data)
        print(self.rates)

    def convert(self, from_currency, to_currency, amount):
        if from_currency != 'USD':
            amount /= self.rates[from_currency]
        amount = round(amount * self.rates[to_currency], 4)
        return amount

    @staticmethod
    def refresh_rates(url):
        data = requests.get(url).json()
        rates = data['rates']
        return data, rates
