#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json, pprint

class AOS8Auth():
    """
    This class requests and stores an authentication cookie for CPPM
    Switch Software.
    """
    def __init__(self, aosip, username, password):
        url_login = "https://" + aosip + ":4343/v1/api/login"
        version = "v1"
        #payload_login = '{\"username\": \"' + username + '\", \"password\": \"' + password + '\"}'
        payload_login = 'username=' + username + '&password=' + password
        # print("URL: ", url_login)
        # print("payload: ", payload_login)
        headers = {'Content-Type': 'application/json'}
        get_uidaruba = requests.post(url_login, data=payload_login, headers=headers, verify=False)
        if get_uidaruba.status_code != 200:
            #print(vars(get_uidaruba))
            print('Status:', get_uidaruba.status_code, 'Headers:', get_uidaruba.headers,
                  'Error Response:', get_uidaruba.reason)
            exit()
        uidaruba = get_uidaruba.json()["_global_result"]['UIDARUBA']
        self.uidaruba = uidaruba
        self.aosip = aosip
        self.version = version


    def logout(self):
        url_login = "http://" + self.ipaddr + "/rest/v1/login-sessions"
        headers = {'uidaruba': self.uidaruba}
        r = requests.delete(url_login, headers=headers)
        return r.status_code
