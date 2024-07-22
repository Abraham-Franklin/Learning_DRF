import requests
import json

url1 = "http://127.0.0.1:8000/api/v1/tasks/1/"
url2 = "http://127.0.0.1:8000/api/v1/tasks/2/"

response = requests.get(url1)
result = response.json()
print(result)
print(response.status_code)
print("I'm Working")



# def get_api_status(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         result = response.json()
#         print(f"Success: {result}")
#     else:
#         print(f"Failed to get data: {response.status_code}")

#     print("I'm Working")

# get_api_status(url1)
# get_api_status(url2)