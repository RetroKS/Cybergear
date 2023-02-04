from datetime import date

today=date.today()

current_year = today.year

dict_main = {"Gaziz B": date(1987, 10, 1) ,"Salamat I": date(1988, 8, 1) ,"Marat T": date(1989, 6, 22) ,"Adilkhan": date(1988, 11, 19), "Ardak": date(1991, 10, 16), "Mama": date(1954, 2, 20), "Papa": date(1956, 5, 9), "Kuralay": date(1992, 5, 5), "Ayzere": date(2018, 8, 24), "My": date(1989, 3, 22), "Almaz A": date(1988, 11, 3)}

print("Birthday List")
col1 = " "
col2 = "Date of Birth"
col3 = "Days left"


dict2 = {}

for key, value in dict_main.items():
	diff = date(today.year, value.month, value.day) - today
	
	dict2[key] = diff.days

sorted_tuple = sorted(dict2.items(), key=lambda x:x[1])
dict2_m = dict(sorted_tuple)

# print(dict2_m)

dict_work = {}
for key, value in dict2_m.items():
	dict_work[value] = {key: dict_main[key]}

# print("\n", dict_work)


print(f"{col1:<10}", f"{col2:^20}", f"{col3:^15}")

for key, value in dict_work.items():
	
	for key, value in value.items():

		diff = date(current_year, value.month, value.day) - today
		
		clean_diff = str(diff).replace(', 0:00:00','')
		# print(clean_diff)

		print(f"{key:<10}{value.strftime('%d %b'):^20}{clean_diff:>14}")


	# diff = date(current_year, value[key].month, value[key].day) - today
	# print(diff)
	# clean_diff = str(diff).replace(', 0:00:00','')
	# print(clean_diff)
	#print(f"{key:<10}{str(value):^20}{clean_diff:>14}")
	# print(f"{key:<10}{value.strftime('%d %b'):^20}{clean_diff:>14}")
	#print("\n")


# for key, value in dict_main.items():

	

# 	#diff = today - value
	
# 	diff = date(current_year, value.month, value.day) - today
# 	clean_diff = str(diff).replace(', 0:00:00','')
# 	#print(f"{key:<10}{str(value):^20}{clean_diff:>14}")
# 	print(f"{key:<10}{value.strftime('%d %b'):^20}{clean_diff:>14}")
# 	#print("\n")


