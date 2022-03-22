import pickle
friends = {"Dan": [20, "London", 23343], "Maria": [34, "Minsk", 456324]}

with open('fiends.dat', 'wb') as f:
	pickle.dump(friends, f)

with open('fiends.dat', 'rb') as f:
	obj = pickle.load(f)
	print(type(obj))
	print(obj)
