import requests
experience = 2
response = requests.get("http://127.0.0.1:8000/predict?experience={}".format(experience))
output = response.json()
print(output)