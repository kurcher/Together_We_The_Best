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



def conv(course, count_of_grn, count_of_dollars, to_grn):
    if to_grn == 'to_grn':

     conv_from_d_to_g = int(float(count_of_dollars)*course)
     rounded_1 = round(conv_from_d_to_g, 2)
     print(rounded_1)
    else:
        conv_from_g_to_d = (float(count_of_grn)/course)
        rounded_2 = round(conv_from_g_to_d, 2)

        print(rounded_2)
convertor_of_value = True
while convertor_of_value:
    def convertor():
        rate = get_usd_to_uah_rate()
        print ('Welcome to the course convertor grn to dollars and dollars to grn')
        to_grn_or_to_dollar_or_course = input(str('Type you want to convert to grn/dollar or you just to know the course. Type "off" to off the course convertor'))
        if to_grn_or_to_dollar_or_course == 'off':
            global convertor_of_value
            convertor_of_value = False
        elif to_grn_or_to_dollar_or_course == 'to_grn':
            dollars = input('Type here how much dollars u want to convert to grn')
            grns = 0
            converted = conv(rate, grns, dollars, to_grn_or_to_dollar_or_course)
        elif to_grn_or_to_dollar_or_course == 'course':
            print(f'The NBU information says that the course now is {rate}')
        else:
            grns = input('Type here how much grn u want to convert to dollars')
            dollars = 0
            converted = conv(rate, grns, dollars, to_grn_or_to_dollar_or_course)




    convertor()