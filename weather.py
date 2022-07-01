#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:02:13 2022

@author: lenovo
"""

import requests
import datetime
import sqlite3


def proccess_data(data):
    return [data['name'],
            data['sys']['country'],
            data['weather'][0]['main'],
            data['weather'][0]['icon']]


def weather(lat='35.715', lon='51.404', appid='0ba870d2feeb31ce3e65df98f16623ff'):
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    r = requests.get(url+'lat='+lat+'&lon='+lon+'&appid='+appid)
    return proccess_data(r.json())


def date():
    data = (datetime.date.isoformat(datetime.date.today()))
    return data


def sql_connector(path):
    cnx = sqlite3.connect(path)
    corsor = cnx.cursor()
    return cnx, corsor


def create_table(cnx, cursor):
    query = 'CREATE TABLE IF NOT EXISTS weather (date text, city text, country text, main text, icon text);'
    cursor.execute(query)
    cnx.commit()


def insert_data(date, city, country, main, icon):
    query = "INSERT INTO weather VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')" % (
        date,
        city,
        country,
        main,
        icon)
    cursor.execute(query)
    cnx.commit()


path = 'Database.db'
cnx, cursor = sql_connector(path)
create_table(cnx, cursor)
date = date()
city, country, main, icon = weather()
insert_data(date, city, country, main, icon)
