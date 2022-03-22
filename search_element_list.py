protocolList = ["FTP", "HTTP", "SNMP", "SSH"]
toFind = "SSH"
found = False
for i in range(len(protocolList)):
	found = protocolList[i] == toFind
	if found:
	   break
if found:
	print("element found at index", i)
else:
	print("element not found")
