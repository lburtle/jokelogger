#!/usr/bin/python3

import requests
import json
import logging

url ="https://official-joke-api.appspot.com/random_joke"

response = request.get(url)

#Load the response into JSON
response = json.loads(response.text)

id = response['id']
setup = response['setup']
punchline = response['punchline']


print(id, setup, punchline)
