#!/usr/bin/env python3

import requests, json
from pycppm import auth


def get_session(access_token):
    #print("AuthAcessToken:", access_token)
    url_session = 'https://cppm.home.rozebud.com/api/session'
    headers = {'Accept': "application/json", 'Authorization': "Bearer " + access_token['access_token']}
    r = requests.get(url_session, headers=headers)
    #print(r.status_code, r.reason)

    cppmrep = json.loads(r.text)['_links']

    return cppmrep
