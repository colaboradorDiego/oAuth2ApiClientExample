from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

import json


#loads JSON from a file.
print("Reading from file")
with open('app.ini', 'r') as f:
    connDATA = json.load(f)

print()
print('Setup from json conf file')
print('Loading connection parameters')
print()
#Comment prints to get a clear screen
print("API credentials")
print()
print('... OAuthUser.name', connDATA['oAuthUser']['name'])
print('... OAuthUser.pass', connDATA['oAuthUser']['passwd'])
print()
print("User credentials")
print()
print('... User.name', connDATA['user']['name'])
print('... User.pass', connDATA['user']['passwd'])
print()
print("Some more params")
print()
print('... API.name', connDATA['api']['name'])
print('... API.token', connDATA['api']['token_url'])
print('... API.base', connDATA['api']['base_url'])


oauth = OAuth2Session(client=LegacyApplicationClient(client_id=connDATA['oAuthUser']['name']))

token = oauth.fetch_token(
    token_url=connDATA['api']['token_url'],
    username=connDATA['user']['name'],
    password=connDATA['user']['passwd'],
    client_id=connDATA['oAuthUser']['name'],
    client_secret=connDATA['oAuthUser']['passwd'],
    verify=False
)

print(token)
