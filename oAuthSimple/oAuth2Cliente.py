import json
import sys
import os

from oauthlib.oauth2 import LegacyApplicationClient

from requests_oauthlib import OAuth2Session

from utiles.utiles import *


"""
from API auth requiremetns we must set:
  grant_type    = password
  ssl           = false
  Content-Type  = application/x-www-form-urlencoded
  cache-control = no-cache

oauthlib.oauth2.LegacyApplicationClient is a perfect client for this job
  it use grant_type password
  it make a request to the token endpoint by adding parameters using the "application/x-www-form-urlencoded" format
"""
# TODO set chache-control in header
# TODO drive errors https://stackoverflow.com/questions/48472298/how-to-capture-api-failure-while-using-oauthlib-oauth2-fetch-token
def connect(conArgs):

    myClient = LegacyApplicationClient(client_id=conArgs['api']['user'])
    mySession = OAuth2Session(client=myClient)

    myToken = mySession.fetch_token(
        token_url='https://' + conArgs['login']['host'] + conArgs['api']['tokenUrl'],
        username=conArgs['login']['user'],
        password=conArgs['login']['pass'],
        client_id=conArgs['api']['user'],
        client_secret=conArgs['api']['pass'],
        verify=False)

    return myToken




def startApp(conArgs):
    showConf(conArgs)
    myToken = connect(conArgs)
    showToken(myToken)


def main(argv):
    # loads JSON from a file.

    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'appOmsApi.ini')), 'r') as f:
        conArgs = json.load(f)
    startApp(conArgs)

def init():
    if __name__ == '__main__':
        sys.exit(main(sys.argv))

init()
