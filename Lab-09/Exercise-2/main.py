
import json
import requests_unixsocket

# Sources: 
# https://docs.docker.com/engine/api/v1.40/#section/Authentication 
# https://github.com/msabramo/requests-unixsocket

if __name__ == '__main__':
    session = requests_unixsocket.Session()

    r = session.get('http+unix://%2Fvar%2Frun%2Fdocker.sock/containers/json')
    print(r.json())
