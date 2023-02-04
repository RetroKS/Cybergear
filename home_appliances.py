import datetime
from datetime import date
import json
# import ast

from dateutil.relativedelta import relativedelta


app1 = "Water Filter"
app2 = "Vacuum cleaner"

list_filters = ["K2", "K5", "K7M", "KO-100S"]
today = date.today()


K5_t = datetime.timedelta(days = 180)
K2_t = datetime.timedelta(days = 180)
K7M_t = datetime.timedelta(days = 545)
KO_100S_t = datetime.timedelta(days = 365*2)

dict_file = '/home/retro/Desktop/Projects_Main/Jarvis/home_appliances.json'
with open(dict_file) as dict_var:
    dict_main = json.load(dict_var)

# print(dict_main)    


print("\nHome appliances service is running on...\n")

option = input(f"Choose:\n\n1. {app1}\n2. {app2}\n\nFor {app1} Enter 1, for {app2} Enter 2\n\n")

col1="Date"
col2="Changed Parts"
col3="Price"

dict_next = {}
dict_next2 = {}

if option == "1":
    print(f"\nNext change for {app1} is as follows:\n")

    # print(dict_main[app1])
    for i in range(len(list_filters)):
        n = len(dict_main[app1]) - 1
        
        
        if list_filters[i] in dict_main[app1][n][1]:
            dict_next[list_filters[i]]=dict_main[app1][n][0]

        while list_filters[i] not in dict_main[app1][n][1]:
            n -= 1
            if n < 0:
                print('break')
                break 
            
            if list_filters[i] in dict_main[app1][n][1]:
                dict_next[list_filters[i]]=dict_main[app1][n][0]
                break

                      
    # print(f"This is the dict_next {dict_next}")
    # datetime_object = datetime.strptime(date_str, '%Y-%m-%d')
    
    for key, value in dict_next.items():
        if key == "K2":
            t = K2_t
        if key == "K5":
            t = K5_t
        if key == "K7M":
            t = K7M_t
        if key == "KO-100S":
            t = KO_100S_t            

        dict_next2[key] = str(t - (today - datetime.datetime.strptime(value, '%Y-%m-%d').date())) 
    # print(f"This is the dict_next2 {dict_next2}")
    col11 = "Filter type"
    col22 = "Remaining days"
    
    print(f"{col11:<10}{col22:^20}")
    for key, value in dict_next2.items():
        print(f"{key:<10}{value.replace(', 0:00:00',''):^20}")    
    # print(K2_t - (today - datetime.datetime.strptime(value, '%Y-%m-%d').date()))
    



    # print(f"{app1} Info\n")
    for key, value in dict_main.items():
        print(f"\n{key} maintenance points:\n")
        print(f"{col1:<10}{col2:^29}{col3:^25}")
        for i in range(len(dict_main[key])):
            print(f"{dict_main[key][i][0]:<10}{str(dict_main[key][i][1]):^30}{dict_main[key][i][2]:^25}")


    var_y = input("\n\nIf you want to add info please enter Y, else enter N\n\n")
    if var_y == "Y":
        input1 = input("Please enter change date in format yyyy-m-d\n\n")
        input2 = input("Please enter filters changed. Titles are: K2, K5, K7M, KO-50\n\n")
        input3 = input("Please enter the total price of the changed filters\n\n")
        
        dict_main[app1].append([input1, input2.split(" "), f'{input3} KZT'])
    

        with open('/home/retro/Desktop/Projects_Main/Jarvis/home_appliances.json', 'w') as jfile:
            json.dump(dict_main, jfile)

        print("\nChanges are saved.")

        print("\nHere is you updated info:\n")

        for key, value in dict_main.items():
            print(f"{key} maintenance points\n")
            print(f"{col1:<10}{col2:^20}{col3:^15}")
            for i in range(len(dict_main[key])):
                print(f"{dict_main[key][i][0]:>25}{str(dict_main[key][i][1]):^29}{dict_main[key][i][2]:^20}")
    

    print(f"\nNext change for {app1} is as follows:\n")

    # print(dict_main[app1])
    for i in range(len(list_filters)):
        n = len(dict_main[app1]) - 1
        
        
        if list_filters[i] in dict_main[app1][n][1]:
            dict_next[list_filters[i]]=dict_main[app1][n][0]

        while list_filters[i] not in dict_main[app1][n][1]:
            n -= 1
            if n < 0:
                print('break')
                break 
            
            if list_filters[i] in dict_main[app1][n][1]:
                dict_next[list_filters[i]]=dict_main[app1][n][0]
                break    
    
    for key, value in dict_next.items():
        if key == "K2":
            t = K2_t
        if key == "K5":
            t = K5_t
        if key == "K7M":
            t = K7M_t
        if key == "KO-100S":
            t = KO_100S_t            

        dict_next2[key] = str(t - (today - datetime.datetime.strptime(value, '%Y-%m-%d').date())) 
    # print(f"This is the dict_next2 {dict_next2}")
    col11 = "Filter type"
    col22 = "Remaining days"
    
    print(f"{col11:<10}{col22:^20}")
    for key, value in dict_next2.items():
        print(f"{key:<10}{value.replace(', 0:00:00',''):^20}")


    if var_y == "N":
        print("\nExiting from service...\n")
if option == "2":
    print("\nVaccuum Cleaner was chosen...")    

