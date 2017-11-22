#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


def get_container(auth):
    """
    Function to get list of mac-addresses from Aruba OS switch
    :param auth:  AOSSAuth class object returned by pyarubaoss.auth
    :return list of mac-addresses
    :rtype list
    """
    #headers = {'cookie': auth.uidaruba}
    params = {'UIDARUBA': auth.uidaruba}
    aoscookie = dict(SESSION = auth.uidaruba)

    url = "https://" + auth.aos8ip + ":4343/v1/configuration/container"
    try:
        r = requests.get(url, verify=False, cookies=aoscookie, params=params)
        container = json.loads(r.text)
        return container
    except requests.exceptions.RequestException as error:
        return "Error:\n" + container.status_code + " get_container: An Error has occured"


    aoscookie = dict(SESSION = auth.uidaruba)
    cmdGetContainer= (requests.get(getContainer, cookies=aoscookies, verify=False))
