import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.select('table tbody tr td.titleColumn a')
first10 = links[:10]
for anchor in first10:
	print(anchor.text)