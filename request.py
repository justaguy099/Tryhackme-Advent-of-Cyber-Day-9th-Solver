import requests

path = 'f'
host = 'http://10.10.169.100:3000/'

while(path != "end"):
	response = requests.get(host+path)
	print(response.json(), end = ' ')
	path = input("whats next?:")	
	

	

