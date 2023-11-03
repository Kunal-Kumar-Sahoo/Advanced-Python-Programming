import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')

if response.status_code != 200:
    print('Error fetching page')
    exit()
else:
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    print('Title:', soup.title.text)
