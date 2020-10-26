import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone'
res = requests.get(url)
print(res)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)

# print(soup.select('p'))

#print(soup.select('.title'))

'''
because it's a list we can get all text simply, either we can only get the text of a single
element of the list or to get text of all the elements we have to use the loop
'''

name = soup.select('.title')
for i in range(0,len(name)):
    price = soup.select('.price')[i].text
    name = soup.select('.title')[i].get_text()
    description = soup.select('.description')[i].get_text()
    print(name)
    print(description)
    print(price, end='\n\n')