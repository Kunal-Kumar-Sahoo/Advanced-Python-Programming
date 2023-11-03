from bs4 import BeautifulSoup

html_content = '''
<div class=\'container\'>
    <p class=\'text\'>Hello World</p>
</div>
'''

soup = BeautifulSoup(html_content, 'html.parser')

paragraph = soup.find('p', class_='text')
paragraph = soup.find('div', class_='container')

print(paragraph.p.text)