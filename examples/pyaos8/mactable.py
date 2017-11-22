#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


def get_mactable(auth):
    """
    Function to get list of mac-addresses from Aruba OS switch
    :param auth:  AOSSAuth class object returned by pyarubaoss.auth
    :return list of mac-addresses
    :rtype list
    """
    headers = {'cookie': auth.uidaruba}
    aoscookie = dict(SESSION = auth.uidaruba)
    url_mactable = "http://" + auth.aos8ip + "/rest/v1/mac-table"
    try:
        r = requests.get(url_mactable, verify=False, headers=headers)
        #mactable = json.loads(r.text)['mac_table_entry_element']
        mactable = r
        print(mactable)
        return mactable
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_mactable: An Error has occured"
