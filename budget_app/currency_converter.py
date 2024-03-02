# currency_converter.py
import requests

def convert_currency(amount, from_currency, to_currency):
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}')

    if response.status_code != 200:
        return None  # Could not fetch rates

    rates = response.json().get('rates')
    to_rate = rates.get(to_currency.upper())

    if to_rate is None:
        return None  # Could not find to_currency

    return amount * to_rate