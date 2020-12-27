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


# conn = OAuth2Session.fetch_token
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


def makePostRequest(myClient, endPoint, myParams, myHeader):
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
    makePostRequest(myClient, endPoint, myParams, myHeader)


# 13.3.
def preciosIndice(connDATA, myClient, myHeader):
    endPoint = connDATA['api']['base_url'] + connDATA['endpoitn']['13.3']
    myParams = {'name': 'M'}
    makePostRequest(myClient, endPoint, myParams, myHeader)


# 13.25.
def getMarKetData(connDATA, myClient, myHeader):
    endPoint = connDATA['api']['base_url'] + connDATA['endpoitn']['13.25']
    myParams = {
        'marketId': 'BYMA',
        'symbol': 'DOAGO2'
    }
    makeGetRequest(myClient, endPoint, myParams, myHeader)
