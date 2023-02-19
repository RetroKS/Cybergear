import sqlite3
import pandas as pd
import datetime


# #Database establishment
# connection = sqlite3.connect("new_vehicle.db")
# cursor = connection.cursor()

data_struct1 = {"Regnumber": ["384ZCI01"], "Color": ["Grey"], "Engine_Power": ["114kW"], "Engine_vol": [1999], "Mass": [1754]}
data_struct2 = {"Point1": [datetime.date(2021, 1, 1), 10700, ["Oil", "Oil Filter"]], "Point2": [datetime.date(2022, 1, 1), 20300, ["Oil", "Oil Filter", "Spark Plugs"]]}


class Vehicle():
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def __repr__(self):
        return self.model, self.year

    def set_characteristics(self, dct):
        self.characteristics = dct

    def get_characteristics(self):
        dct1 = self.characteristics
        dct1["model"] = self.model
        dct1["year"] = self.year

        df = pd.DataFrame(dct1)

        return df

    def get_maintenance_points(self):
        dct2 = data_struct2

        df = pd.DataFrame(dct2, index = ["Date", "Price", "Consumables"])

        return df    
           
sportage = Vehicle("Kia Sportage IV", 2020)  
sportage.set_characteristics(data_struct1) 

print(sportage.get_characteristics())
print(sportage.get_maintenance_points())




# # Create table named Maintenance_points
# cursor.execute("""CREATE TABLE Maintenance_points (datetime.date TEXT, cost INTEGER, consumable TEXT) """)



# #Insert row of values into new_table
# cursor.execute(f""" INSERT INTO Maintenance_points VALUES("{sportage.date}", {sportage.cost}, "{sportage.consumable}")""")

# #Commit changes to database
# connection.commit()

# #Close connection to database
# connection.close()

