import requests
from bs4 import BeautifulSoup

# url = 'https://github.com/Kunal-Kumar-Sahoo'
url = 'https://example.com'
response = requests.get(url)

print('Response Text:', response.text)

soup = BeautifulSoup(response.text, 'html.parser')

print('Page title:', soup.title.text)