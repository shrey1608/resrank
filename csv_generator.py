import csv

from itertools import zip_longest
row_list = []
while 1:
	print("Do you want to add column ?")
	print("Type yes or no")
	ans = input()
	if(ans == "yes"):
		print("Specify the column name")
		trow = []
		col_name = input()
		trow.append(col_name)
		while(1):
			print("Add keyword to this column : type yes or no")
			query = input()
			if query == "no":
				break
			elif query == "yes":
				print("Type the keyword")
				keyword = input()
				trow.append(keyword)
			else:
				print("Invalid input")

		row_list.append(trow)
	elif ans == "no":
		break
	else:
		print("Invalid input")
		continue

export_data = zip_longest(*row_list, fillvalue='')
print(row_list)
with open('resume_dataset.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerows(export_data)

file.close()
