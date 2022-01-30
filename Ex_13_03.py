import urllib.request, urllib.parse, urllib.error
import ssl

#  api_key = False
#  If you have a Google Places API key, enter it here
#  api_key = 'AIzaSy___IDByT70'
#  https://developers.google.com/maps/documentation/geocoding/intro


#  if api_key is False:
#    api_key = 42
 #   serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
#  else:
#    serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'http://py4e-data.dr-chuck.net/comments_1457352.xml'
url = urllib.request.urlopen(address, context = ctx).read()
tree = ET.fromstring(url)

counts = tree.findall('comments/comment')
result = 0
for count in counts:
    x = count.find('count').text
    result = result + int(x)
print('Quantity :', result)
