from bs4 import BeautifulSoup

html_content = '''
<html>
    <head>
        <title>My Webpage</title>
    </head>
    <body>
        <p>Hello, World!</p>
    </body>
</html>
'''
soup = BeautifulSoup(html_content, 'html.parser')

print('Title:', soup.title)
print('Paragraph:', soup.p.text)
# print(soup)