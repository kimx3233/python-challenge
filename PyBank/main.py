import os
import csv

csv_path = os.path.join("..", "Resources", "budget_data.csv")

with open(csv_path, newline = '') as csvfile:
	csvread = csv.reader(csvfile, delimiter = ",")
	print(next(csvread))
 
	Total_Month = 0
	Net_Amount = 0
	Avg_Change = 0
	
	
	for row in csvread:
		Total_Month += 1
		Net_Amount += int(row[1])
		
		
	print("Total Month: " + str(Total_Month))
	print("Total: $" + str(Net_Amount))
		
	
	net = 0
	diff = 0
	data_list = list(csvread)
	max_change = 0
	max_date = ""
	min_date = ""
	min_change = 0
	for i, row in enumerate(data_list):
		if i >= 1:
			net += int(row[1])

		if i >= 2:
			temp = int(row[1]) - int(data_list[i-1][1])
			diff += temp
		if temp >= max_change:
			max_date = row[0]

			max_change = max(temp, max_change)

		if temp <= min_change:
			min_date = row[0]
			min_change = min(temp, min_change)


	tm = len(data_list) - 1
	print("Total Month: " + str(len(data_list) - 1))
	print("Total Net: " + str(net))
	print("avg change: " + str(diff/tm))
	print("max: " + max_date + " " + str(max_change))
	print("min: " + min_date + " " + str(min_change))
	
	 
	
	