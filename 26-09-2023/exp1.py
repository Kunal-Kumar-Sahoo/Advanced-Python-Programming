from bs4 import BeautifulSoup

html_content = '''
<div id=\'content\'>
    <p> Hello, World!</p>
</div>
'''

soup = BeautifulSoup(html_content, 'html.parser')

div = soup.find('div', id='content')
print(div.p.text)