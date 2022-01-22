# https://www.metaweather.com/api/location/2295420/
import requests
response = requests.get('https://www.metaweather.com/api/location/2295420/')

content = response.json()
print(content)
print(content['title'])
print(content['consolidated_weather'][0]['weather_state_name'])
print(round(content['consolidated_weather'][0]['max_temp'], 3))
