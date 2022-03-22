import http.client, sys
domain = sys.argv[1]
connection = http.client.HTTPConnection(domain)
connection.request("GET", "/")
response = connection.getresponse()
print(type(response))
print(response.status, response.reason)

if response.status == 200:
    data = response.read()
    print(data)