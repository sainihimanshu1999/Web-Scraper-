from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'

res = requests.get(url)
print(res)
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup)
# print(soup.find('h1').text)
# print(soup.find('a',{'class':'tag'}).text)

'''
for single element
'''

# lst = []
# lst.append(soup.find_all(class_ = 'tags')[0].text.replace('\n', ' ').strip())
# print(lst[0])


'''
for multiple elements
'''

tags = soup.find_all(class_ = 'tags')
lst = []
for tag in tags:
    lst.append(tag.text.replace('\n',' ').strip())
print(lst)