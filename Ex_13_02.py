import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup as bs

#   http://py4e-data.dr-chuck.net/known_by_Yong.html

url = input('Enter URL: ')
count = int(input('Enter count:'))
position = int(input('Enter position:'))
i = 0

while i < count:
    link = []
    html = urllib.request.urlopen(url).read()
    soup = bs(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        link.append(tag.get('href', None))
    url = link[position - 1]
    print('Retrieving:', url)
    i = i + 1







#  Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#  Enter count: 4
#  Enter position: 3
#  Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#  Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
#  Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
#  Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
#  Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html