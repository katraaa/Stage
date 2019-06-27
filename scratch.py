import urllib.request
import urllib
import json

response = urllib.request.urlopen('https://api.monarchinitiative.org/api/swagger.json')
print('RESPONSE:', response)
print('URL     :', response.geturl())
