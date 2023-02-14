import csv

f = open("G:/Python/Sample.csv",'w')

writer = csv.writer(f)

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']
writer.writerow(header)
while True:
	
	writer.writerow(data)


f.close()