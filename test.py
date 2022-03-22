#a = 0 
#if a: 
# print('x') 
#else: 
# print('y'

#with open('test.txt', 'r') as file:
#	print(file.read())

#f = open('test.txt', 'r')
#f.seek(4)
#content = f.read(5)
#print(content)

with open('test.txt') as file:
	my_list = file.read().splitlines()
	print(my_list)

with open('test.txt', 'r') as file:
	my_list = file.readlines()
	print(my_list)
