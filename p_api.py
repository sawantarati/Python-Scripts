import requests
import json

responce_API = requests.get('https://itunes.apple.com/search?term=metallica&entity=musicVideo')

print(responce_API.status_code)


