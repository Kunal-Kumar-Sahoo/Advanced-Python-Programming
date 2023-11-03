from bs4 import BeautifulSoup

html_content = '<img src="https://example.com/image.jpg" alt="Sample Image">'

soup = BeautifulSoup(html_content, 'html.parser')

image = soup.img

src = image['src']
alt = image['alt']

print('Image source:', src)
print('Image alt text:', alt)