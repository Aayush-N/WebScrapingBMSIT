import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.text[:250])