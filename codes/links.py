from bs4 import BeautifulSoup
import requests

url = 'https://webscraper.io/test-sites/e-commerce/allinone'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

'''
for finding all the anchor tags
'''

# for a_tag in soup.findAll('a'):
#     href = a_tag.attrs.get('href')
#     if href !="":
#         print(href)
#         continue


'''
for finding a specific anchor tag in some specific div
'''

# div = soup.find('div',{'class':'col-sm-4 col-lg-4 col-md-4'})
# a = div.find('a')
# link = a.attrs.get('href')
# print(link)


'''
for finding all the images 
'''

# for a_tag in soup.findAll('img'):
#     href = a_tag.attrs.get('src')
#     if href != '':
#         print(href)
#         continue


'''
for a specific image in a specifi div
'''

div = soup.find('div', {'class' :'col-sm-4 col-lg-4 col-md-4'})
a = div.find('img')
img = a.attrs.get('src')
print(img)