import sqlite3

import datetime
from datetime import date


class Vehicle():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

sportage = Vehicle("Kia Sportage")


class Mpoints():
    def __init__(self, date, cost, consumable):
        self.date = date
        self.cost = cost
        self.consumable = consumable

    def __repr__(self):
        return f"Date: {self.date}/ Consumables: {self.consumable}/ Cost: {self.cost}KZT"     


r1 = Mpoints(date(2021,1,1).strftime('%d %b %y'), 20000, ["Oil", "Oil filter"])    


# print(r1)


# dat = input("Please, enter date in format yyyy-mm-dd:\n")
# cost = input("Please, enter cost:\n")
# consumable = input('Please, enter changed parts:\n')


# mp1 = Mpoints(datetime.datetime.strptime(dat, '%Y-%m-%d'), cost, [consumable])
# print(mp1)

dict_main = {}
list_v = []
list_v.append(r1)

print(list_v)

dict_main[sportage] = list_v
print(dict_main)

# Database establishment
connection = sqlite3.connect("vehicle.db")
cursor = connection.cursor()

# Create table named new_table
cursor.execute("""CREATE TABLE Mpoints (date TEXT, cost INTEGER, consumable TEXT) """)

# Insert row of values into new_table

cursor.execute(f""" INSERT INTO Mpoints VALUES("{r1.date}", {r1.cost}, "{r1.consumable}")""")

# commit changes to database
connection.commit()

# close connection
connection.close()