from bs4 import BeautifulSoup

html_content = '''
<table>
    <tr>
        <th>Name</th>
        <th>Age</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>25</td>
    </tr>
    <tr>
        <td>Bob</td>
        <td>30</td>
    </tr>
</table>
'''

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')

for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    name = columns[0].text
    age = columns[1].text
    print(f'Name: {name}\tAge: {age}')