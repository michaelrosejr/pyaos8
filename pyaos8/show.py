#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def show_ap_database(auth):

    url_showcommand = "https://" + auth.aos8ip + ":4343/v1/configuration/showcommand?json=1&UIDARUBA=" + auth.uidaruba + "&command=" + auth.showcom
    aoscookie = dict(SESSION = auth.uidaruba)
    #print(url_showcommand)
    try:
        r = requests.get(url_showcommand, cookies=aoscookie, verify=False)
        # showdata = json.loads(r.text)['mac_table_entry_element']
        if r.status_code != 200:
            #print(vars(r))
            print('Status:', r.status_code, 'Headers:', r.headers,
                  'Error Response:', r.reason)

        return r.text
    except requests.exceptions.RequestException as error:
        #print("Error")
        return "Error:\n" + str(error) + " get_showcommand: An Error has occured"
