import sqlite3
import datetime

#List of data columns for comprehensive view
data_columns = ["Date", "Cost", "Consumables"]

#Database establishment
connection = sqlite3.connect("vehicle.db")
cursor = connection.cursor()

#Fetching from database all maintenance points
maintenance_data = cursor.execute("SELECT * FROM Mpoints").fetchall()

print(maintenance_data)
print(type(maintenance_data))

# print("These is all Maintenance Points for Kia Sportage\n")

# print(f"{data_columns[0]:<10}{data_columns[1]:^29}{data_columns[2]:^25}\n")


# for point in maintenance_data:
#     print(f"{point[0]:<10}{point[1]:^29}{point[2]:^25}\n")
#     print(type(point[1]))
#     # print(f"{point[0].strftime('%d %b %y'):<10}{point[1]:^29}{point[2]:^25}\n")



class Vehicle():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

sportage = Vehicle("Kia Sportage") 
bmw5 = Vehicle("BMW 5-series")       


# dat = input("Please, enter date in format yyyy, mm, dd:\n")

# sportage.date = datetime.datetime.strptime(dat, '%Y, %m, %d')

# cost = input("Please, enter cost:\n")

# sportage.cost = cost

# consumable = input('Please, enter changed parts:\n')

# sportage.consumable = consumable



# # Create table named new_table
# # cursor.execute("""CREATE TABLE Mpoints (date TEXT, cost INTEGER, consumable TEXT) """)



# #Insert row of values into new_table
# cursor.execute(f""" INSERT INTO Mpoints VALUES("{sportage.date}", {sportage.cost}, "{sportage.consumable}")""")

# #Commit changes to database
# connection.commit()

# #Close connection to database
# connection.close()

# # r1 = Mpoints(date(2021,1,1).strftime('%d %b %y'), 20000, ["Oil", "Oil filter"])    