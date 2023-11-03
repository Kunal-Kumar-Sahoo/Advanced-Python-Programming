from bs4 import BeautifulSoup

html_content = '<div><p>Paragraph1</p><p>Paragraph2</p><p>Paragraph3</p></div>'

soup = BeautifulSoup(html_content, 'html.parser')

d = soup.div
for p in d.find_all('p'):
    print(p.text)