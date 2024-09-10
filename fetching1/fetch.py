import requests
import pandas as pd
import json

url = "http://api.openweathermap.org/data/2.5/weather?&lat=33.3789&lon=35.4839&units=metric&lang=en&appid=a2b2e442aba806b89cc7e799526a1158"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    data1 = pd.json_normalize(data , "weather", "id", "name")
    df = pd.DataFrame(data1)
    data2 = pd.json_normalize(data["main"])
    df1 = pd.DataFrame(data2)
    df2 = pd.concat([df, df1], axis=1)
    df2.to_csv('weather.csv', index = False, float_format="%.2f")
    print(df2)





