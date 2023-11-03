from bs4 import BeautifulSoup

html_content = '''
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
'''

soup = BeautifulSoup(html_content, 'html.parser')

items = soup.find_all('ul')

for item in items:
    print(item.text)
