from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

from oauthlib.oauth2 import FatalClientError, OAuth2Error

import json
import sys
import requests

from utiles.utiles import *

#Stomp version 6.1.0
import stomp


# from API requiremetns we must set:
#  grant_type    = password
#  ssl           = false
#  Content-Type  = application/x-www-form-urlencoded
#  cache-control = no-cache
#
# oauthlib.oauth2.LegacyApplicationClient is a perfect client for this job
#  it use grant_type password
#  it make a request to the token endpoint by adding parameters using the "application/x-www-form-urlencoded" format

# TODO set chache-control in header
def connect(connDATA):

    myClient = LegacyApplicationClient(client_id=connDATA['oAuthUser']['name'])
    mySession = OAuth2Session(client=myClient)

    # TODO drive errors https://stackoverflow.com/questions/48472298/how-to-capture-api-failure-while-using-oauthlib-oauth2-fetch-token
    try:
        conn = mySession.fetch_token(
            token_url=connDATA['api']['base_url'] + connDATA['api']['token_url'],
            username=connDATA['user']['name'],
            password=connDATA['user']['passwd'],
            client_id=connDATA['oAuthUser']['name'],
            client_secret=connDATA['oAuthUser']['passwd'],
            verify=False,
        )
        return conn

    except (FatalClientError) as e:
        print('HEY PUTO FatalClientError')
        return False

    except (OAuth2Error) as e:
        print('HEY PUTO OAuth2Error')
        return False

    except (requests.exceptions.ConnectionError) as e:
        print('HEY PUTO ConnectionError')
        return False

    except (requests.exceptions.RequestException) as e:
        print('HEY PUTO RequestException')
        return False

# Listeners are simply a subclass which implements the methods in the ConnectionListener class
class MyListener():
    # TODO create de listener
    a = 'a'

# Establishing a connection http://jasonrbriggs.github.io/stomp.py/api.html#establishing-a-connection
# To receive messages you need to setup a listener on your connection http://jasonrbriggs.github.io/stomp.py/api.html#sending-and-receiving-messages
def startStompClient(connDATA, myToken):
    #El servidor enviara requests al cliente cada 10seg y esperara uno de respuesta cada 20seg.
    conn = stomp.Connection(
        host_and_ports=[(connDATA['stomp']['host'] + connDATA['stomp']['service'], connDATA['stomp']['port'])],
        use_ssl=False,
        heartbeats=(10000, 20000)
    )

    # Stomp provides a few implementations of listeners, but the simplest is PrintingListener which just prints all interactions between the client and server.
    conn.set_listener('', stomp.PrintingListener())

    myHeader = {
        'Authorization': 'Bearer ' + myToken['access_token']
    }
    conn.connect(
        wait=True,
        headers=myHeader
    )

# main proccess
def startApp(connDATA):
    showConf(connDATA)
    myToken = connect(connDATA)
    showToken(myToken)

    # Como hacer un request a la API REST
    myClient = OAuth2Session(connDATA['oAuthUser']['name'], token=myToken)

    myHeader = {
        'Content-Type': 'application/json',
    }


    startStompClient(connDATA, myToken)

    # 13.2.
    # preciosIndices(connDATA, myClient, myHeader)

    # 13.3.
    # preciosIndice(connDATA, myClient, myHeader)

    # 13.25.
    # getMarKetData(connDATA, myClient, myHeader)




def main(argv):
    # loads JSON from a file.
    with open('app.ini', 'r') as f:
        connDATA = json.load(f)
    startApp(connDATA)

def init():
    if __name__ == '__main__':
        sys.exit(main(sys.argv))

init()


