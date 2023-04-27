
import requests

url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    print("URL:", response.url)
else:
    print("Error:", response.status_code)
