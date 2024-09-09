import requests
import pandas as pd
import json

url = "http://api.openweathermap.org/data/2.5/weather?&lat=33.3789&lon=35.4839&units=metric&lang=en&appid=a2b2e442aba806b89cc7e799526a1158"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()


normalized-data = pd.json-normalize(data)
df = pd.DataFrame(normalized-data)
print(df)
