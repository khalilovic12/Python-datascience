import requests
import datetime
import json
import sqlite3


def get_holidays (code):    
   
    Holidays_list = []
    response = requests.get('https://date.nager.at/api/v2/publicholidays/2017/'+code)
    #print(response.status_code)
    #print((response.json()))
    Holidays_list = response.json()

    return (Holidays_list)
