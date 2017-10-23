#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def show_bindings(auth):

    url = "https://" + auth.aos8ip + ":4343/v1/configuration/showcommand?json=1&UIDARUBA=" + auth.uidaruba + "&command=show ip dhcp binding"
    aoscookie = dict(SESSION = auth.uidaruba)
    #print(url)
    try:
        r = requests.get(url, cookies=aoscookie, verify=False)
        # showdata = json.loads(r.text)['mac_table_entry_element']
        if r.status_code != 200:
            #print(vars(r))
            print('Status:', r.status_code, 'Headers:', r.headers,
                  'Error Response:', r.reason)

        '''
        The following properly formats the JSON returned from the AOS controller into something that is usable.
        '''
        aoslines = json.loads(r.text)['_data']
        aoslines = [i.replace('"', '') for i in aoslines]
        aoslines = [j.replace(",\n", "") for j in aoslines]
        aoslines = [k.replace("  ", "") for k in aoslines]

        bindings = {}
        for line in aoslines:
            columns = line.split(' : ')
            if "lease" in line:
                ip = columns[0].split()[1]
                bindings[ip] = {}
                # bindings[ip] = columns[0].split()[1]
            if "starts" in line:
                bindings[ip]['starts'] = columns[1]
            if "ends" in line:
                bindings[ip]['ends'] = columns[1]
            if "hardware" in line:
                bindings[ip]['mac'] = columns[0].split()[2].replace(';', '')
            if "Transaction" in line:
                bindings[ip]['last access'] = columns[1]
            if "binding state active" in line:
                bindings[ip]['state'] = columns[0].split()[2]
            if "next" in line:
                bindings[ip]['next state'] = columns[0].split()[3]
            else:
                pass

        return bindings
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + "show_ip_dhcp_binding: An Error has occured"
