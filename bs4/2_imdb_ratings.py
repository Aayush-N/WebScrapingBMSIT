import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.select('table tbody tr td.titleColumn a')
ratings = soup.select('table tbody tr td.imdbRating strong')
for anchor, strong in zip(links[:10], ratings[:10]):
	print(anchor.text + ' -> ' + strong.text)