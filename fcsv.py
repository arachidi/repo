import csv
#with open('airtravel.csv', 'r') as f:
#	reader = csv.reader(f)
#	next(reader)
#	year_1958 = dict()
#	for row in reader:
#		year_1958[row[0]] = row[1]

#	print(year_1958)

#	max_1958 = max(year_1958.values())

#	for k, v in year_1958.items():
#		if max_1958 == v:
#			print(f'Busiest Month in 1958:{k}, Flieghts:{v.strip()}')

#Write to CSV
#with open('people.csv', 'a') as csvfile:
#	writer = csv.writer(csvfile)
#	csvdata = (3, 'Anne', 'Amsterdam')
#	writer.writerow(csvdata)

#with open('number.csv' , 'w', newline='') as f:
#	writer = csv.writer(f)
#	writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
#	for x in range(1, 101):
#		writer.writerow([x, x**2, x**3, x**4])

#with open('people2.csv', 'r') as f:
#	reader = csv.reader(f, delimiter=':', lineterminator='\n')
#	for row in reader:
#		print(row)

#CSV Dialects
csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')
with open('items.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, dialect='hashes')

	for row in reader:
		print(row)

with open('items.csv', 'a') as csvfile:
	writer = csv.writer(csvfile, dialect='hashes')
	writer.writerow(('spoon', 3, 1.5))
