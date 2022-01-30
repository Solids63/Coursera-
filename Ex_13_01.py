import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs

url = 'http://py4e-data.dr-chuck.net/comments_1457350.html'
html = urllib.request.urlopen(url).read()
soup = bs(html, 'html.parser')


tags = soup('span')
result = 0
for tag in tags:
    result = result + int(tag.contents[0])
print(result)
