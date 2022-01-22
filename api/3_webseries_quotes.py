# https://web-series-quotes-api.deta.dev/docs
# https://web-series-quotes-api.deta.dev/quote/
import requests
response = requests.get('https://web-series-quotes-api.deta.dev/quote/')

content = response.json()
print(content)
print(content['author'])
print(content['quote'])
print(content['series'])
