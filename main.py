import requests

path = 'f'
host = 'http://10.10.169.100:3000/' #This is the path for the host

while(path != "end"):
	response = requests.get(host+path)
	print(response.json(), end = ' ')
	path = input("whats next?:") #for this input you need to supplement it with the value of 'next' of the json response
	

	

