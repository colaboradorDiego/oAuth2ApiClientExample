from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

import json
import sys

def showConf(connDATA):
    print()
    print('Setup from json conf file')
    print('Loading connection parameters')
    print()
    # Comment prints to get a clear screen
    print("API credentials")
    print('... OAuthUser.name', connDATA['oAuthUser']['name'])
    print('... OAuthUser.pass', connDATA['oAuthUser']['passwd'])
    print()
    print("User credentials")
    print('... User.name', connDATA['user']['name'])
    print('... User.pass', connDATA['user']['passwd'])
    print()
    print("More Stuff")
    print('... API.name', connDATA['api']['name'])
    print('... API.base', connDATA['api']['base_url'])
    print('... API.token', connDATA['api']['token_url'])
    print('... API.stomp', connDATA['api']['stomp_url'])


def showToken(conn):
    print()
    # print(conn)
    print("Connection Status")
    print('... access_token', conn['access_token'])
    print('... token_type', conn['token_type'])
    print('... refresh_token', conn['refresh_token'])
    print('... expires_in', conn['expires_in'])
    print('... scope', conn['scope'])
    print('... expires_at', conn['expires_at'])
    print()

# from API requiremetns we must set:
#  grant_type    = password
#  ssl           = false
#  Content-Type  = application/x-www-form-urlencoded
#  cache-control = no-cache
# oauthlib.oauth2.LegacyApplicationClient
#   Is a client using grant_type password
#   The client makes a request to the token endpoint by adding parameters using the
#   "application/x-www-form-urlencoded" format

# TODO set chache-control in header
def connect(connDATA):

    myClient = LegacyApplicationClient(client_id=connDATA['oAuthUser']['name'])
    mySession = OAuth2Session(client=myClient)

    conn = mySession.fetch_token(
        token_url=connDATA['api']['base_url'] + connDATA['api']['token_url'],
        username=connDATA['user']['name'],
        password=connDATA['user']['passwd'],
        client_id=connDATA['oAuthUser']['name'],
        client_secret=connDATA['oAuthUser']['passwd'],
        verify=False
    )

    return conn


def makeRequest(myClient, endPoint, myParams, myHeader):
    print()
    respuesta = myClient.post(endPoint, data=myParams, headers=myHeader, verify=False)
    print(respuesta)
    print(respuesta.content)

def makeGetRequest(myClient, endPoint, myParams, myHeader):
    print()
    respuesta = myClient.get(endPoint, data=myParams, headers=myHeader, verify=False)
    print(respuesta)
    print(respuesta.content)

# 13.2.
def preciosIndices(connDATA, myClient, myHeader):
    endPoint = connDATA['api']['base_url'] + connDATA['endpoitn']['13.2']
    myParams = {
        'all': False,
        'filters': [
            {'name': 'M'},
            {'name': 'A'}
        ]
    }
    makeRequest(myClient, endPoint, myParams, myHeader)

# 13.3.
def preciosIndice(connDATA, myClient, myHeader):
    endPoint = connDATA['api']['base_url'] + connDATA['endpoitn']['13.3']
    myParams = {'name': 'M'}
    makeRequest(myClient, endPoint, myParams, myHeader)

# 13.25.
def getMarKetData(connDATA, myClient, myHeader):
    endPoint = connDATA['api']['base_url'] + connDATA['endpoitn']['13.25']
    myParams = {
        'marketId': 'BYMA',
        'symbol': 'DOAGO2'
    }
    makeGetRequest(myClient, endPoint, myParams, myHeader)




def startApp(connDATA):
    showConf(connDATA)
    myToken = connect(connDATA)
    showToken(myToken)

    # Como hacer un request a la API REST
    myClient = OAuth2Session(connDATA['oAuthUser']['name'], token=myToken)

    myHeader = {
        'Content-Type': 'application/json',
    }

    # 13.2.
    # preciosIndices(connDATA, myClient, myHeader)

    # 13.3.
    # preciosIndice(connDATA, myClient, myHeader)

    # # 13.25.
    getMarKetData(connDATA, myClient, myHeader)




def main(argv):
    # loads JSON from a file.
    with open('app.ini', 'r') as f:
        connDATA = json.load(f)
    startApp(connDATA)

def init():
    if __name__ == '__main__':
        sys.exit(main(sys.argv))

init()


