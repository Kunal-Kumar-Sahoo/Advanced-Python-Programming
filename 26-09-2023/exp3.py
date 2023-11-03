from bs4 import BeautifulSoup

html_content = '<a href=\'https://example.com\'>Visit Example.com</a>'

soup = BeautifulSoup(html_content, 'html.parser')

link = soup.a
print('Link Text:'. link.text)
print('Link URL:'. link['href'])