from bs4 import BeautifulSoup
import requests

html_content = requests.get('https://www.w3schools.com/python/python_regex.asp').text

soup = BeautifulSoup(html_content, 'html.parser')

images = soup.find_all('img')
tables = soup.find_all('table')


for img in images:
    print('Src:', img['src'])
    print('Alt', img['alt'])

for i, table in enumerate(tables):
    print(i+1, end='\t')
    for col in table.find('tr').find_all('th'):
        print(col.text, end='\t')
    print()
