import socket
import sys

try:
	result = socket.gethostbyaddr(sys.argv[1])
	print("the host name is: ", result[0])
	print("ip addresses:")
	for item in result[2]:
		print(" "+item)
except socket.error as e:
	print("Error for resolving ip address:", e)
