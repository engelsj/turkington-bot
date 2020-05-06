import os
import requests

api_key = os.environ.get('movieApiKey')
parameters = {'t':'Dark Knight', 'apikey': api_key}
resp = requests.get('http://www.omdbapi.com/', params=parameters)

print(resp.text)
