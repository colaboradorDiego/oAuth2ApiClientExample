# oAuth2ApiClientExample
A simple example OAuth 2.0 client written in Python for dummies

# oAuth1 & oAuth2 Protocols
OAuth 1.0/2.0 is the industry-standard protocol for authorization. OAuth 2.0 focuses on client developer simplicity.
	OAuth for dummies -> recomendamos la lectura de "presentation/Oauth2.pdf"
	
	
# Authlib for python
OAuthLib is a framework which implements OAuth1 & OAuth2 without assuming a specific HTTP request object or web framework.
	procject -> https://pypi.org/project/oauthlib/
	Resource Owner Password Flow -> https://auth0.com/docs/flows/call-your-api-using-resource-owner-password-flow
	doc's https://oauthlib.readthedocs.io/en/latest/index.html

# requests-oauthlib for python
Requests-OAuthlib uses Requests and OAuthlib libraries to provide an easy Python interface for building OAuth1 and OAuth2 clients.
	project -> https://pypi.org/project/requests-oauthlib/
	doc's https://requests-oauthlib.readthedocs.io/en/latest/index.html
	
# ejercicios luego de las lecturas
	oAuthSimple -> Cliente oAuth2 bien basico y por consola
				-> Progamado teniendo en cuanta autenticar contra OMS BYMA
				-> parametros = jsonSample.ini (parametros tiene que tener esta estructura jSon)
				-> jsonSample tiene que tener usuarios y claves correctas.
	
	OAuthFlask -> El mismo cliente anterior pero se metio el flask en el medio.
			   -> Aun no se bien como llegue aca pero vamos a tratar que funcione
			   -> Aun no funciona
			   
## 1. Resultados de la siguiente busqueda en github: "oauth client example"

https://github.com/Signafire/oauth-client-example-python/blob/master/requirements.txt
	rauth==0.7.0
	requests==2.2.1
	wsgiref==0.1.2

https://github.com/Fisherworks/example-oauth2-client/blob/master/requirements.txt
	Flask
	Authlib
	requests
	
https://github.com/shimniok/example-oauth-server-client/blob/master/requirements.txt
	Flask
	Flask-SQLAlchemy
	Authlib
	requests
	requests-oauthlib
	
https://github.com/rohe/client-cred-oauth2-rp
https://github.com/rohe/ojou_course/tree/master/presentation


https://github.com/Tosha1409/discogs_client_example_Python3


https://github.com/benetech/bookshare-webpy-3-legged-oauth2-public

https://github.com/vastevenson/vs-youtube-auth-example


## 2. Tools, libs & frameworks

Fiddler
*******
https://www.telerik.com/fiddler/usecases/https-traffic-recording

WireShark
**********
https://wiki.wireshark.org/CaptureFilters

Flask
*****
Es un micro framework para programar aplicaciones web en pyhon. Es del lado servidor que corre, mas que nada preciso:
	"pyhon rest client"

	
rauth
*****
ES UNA PORONGA ESTA BOSTA -> SWITCH TO oauthlib
A simple Python OAuth 1.0/a, OAuth 2.0, and Ofly consumer library built on
top of Requests.	
> Project: https://pypi.org/project/rauth/
> Docs: https://rauth.readthedocs.io/en/latest/


# HTTP METHODS
CONNECT -> https://developer.mozilla.org/es/docs/Web/HTTP/Methods/CONNECT


# Network Capture Tools for API Developers
Introduccion -> https://developers.google.com/gdata/articles/wireshark

