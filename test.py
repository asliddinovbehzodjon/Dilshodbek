from urllib import response
import requests
import json
BASE_URL ='https://dilshodbekdb.pythonanywhere.com/api/v1'
name=str(input("Enter name: "))
response = requests.get(f"{BASE_URL}/get/{name}")
rest= json.loads(response.text)
print(rest)
