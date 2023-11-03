from bs4 import BeautifulSoup
import requests

for page in range(1, 4):
    url = f'https://example.com/page/{page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(f'Paragraphs in URL{page}>>>')
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        print(paragraph.text)

    print(f'Headings in URL{page}>>>')
    headings = soup.find_all(['h1', 'h2'])
    for heading in headings:
        print(heading.text)
    
    print(f'Scraping done for URL{page}')