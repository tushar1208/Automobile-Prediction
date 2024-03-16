import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'engine_size':130, 'city_mpg':1})

print(r.json())
