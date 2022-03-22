import json
friends = {"Dan": [20, "London", 23343], "Maria": [34, "Minsk", 456324]}

with open('friends.json', 'w') as f:
	json.dump(friends, f, indent=4)

json_string = json.dumps(friends, indent=1)
print(json_string)
