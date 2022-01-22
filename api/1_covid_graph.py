#https://corona.dnsforfamily.com/graph.png?c=IN

import requests

response = requests.get('https://corona.dnsforfamily.com/graph.png?c=IN')

file = open('image.png', 'wb')
file.write(response.content)