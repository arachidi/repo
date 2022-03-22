import http.client
import sys

connection = http.client.HTTPConnection(sys.argv[1])
connection.request("GET", "/")
response = connection.getresponse()
print(type(response))
print(response.status, response.reason)
if response.status == 200:
	data = response.read()
	print(data)
