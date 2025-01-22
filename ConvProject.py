import json
from urllib.request import urlopen
import tkinter as tk
from tkinter import messagebox


def get_usd_to_uah_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    try:
        with urlopen(url) as response:
            data = json.loads(response.read().decode())
            for currency in data:
                if currency['cc'] == 'USD':
                    return currency['rate']
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        return None
def conv_to_uah(rate, count_of_usd):
    conv_from_usd_to_uah = int(float(count_of_usd)*rate)
    rounded_1 = round(conv_from_usd_to_uah, 2)
    print(rounded_1)
def conv_to_usd(rate, count_of_uah):
    conv_from_uah_to_usd = (float(count_of_uah)/rate)
    rounded_2 = round(conv_from_uah_to_usd, 2)
    print (rounded_2)
def convertor():
        rate_of_usd = get_usd_to_uah_rate()
        print ('Welcome to the course convertor grn to dollars and dollars to grn')
        to_uah_or_to_usd_or_course = input(str('Type you want to convert to uah/usd or you just to know the course. Type "off" to off the course convertor'))
        if to_uah_or_to_usd_or_course == 'to uah':
            usd = input('Type here how much dollars u want to convert to grn')
            uah = 0
            converted_to_uah = conv_to_uah(rate_of_usd, usd)
        elif to_uah_or_to_usd_or_course == 'off':
            return None
        elif to_uah_or_to_usd_or_course == 'course':
            print(f'The NBU information says that the course now is {rate_of_usd}')
        else:
            uah = input('Type here how much grn u want to convert to dollars')
            usd = 0
            converted_to_usd = conv_to_usd(rate_of_usd, uah)
convertor()