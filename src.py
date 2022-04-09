import re

file_path = 'access.log'
with open(file_path, 'r') as open_file:
	line = open_file.read()

print(line)

m = re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line)
result = m.group('IP')
print(result)


