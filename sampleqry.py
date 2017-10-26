#!/usr/bin/env python3
import sys
import json
import requests
import datetime
import time
import os
import logging
import pprint
import yaml

from pyaos8 import auth
import pyaos8.apdatabase as apdatabase
import pyaos8.show as show
import pyaos8.mactable as mactable
import pyaos8.container as container
#import pyaos8.session as session
import pyaos8.show_ip_dhcp_binding as show_bindings
import pyaos8.dhcp_pool as dhcppool
import pyaos8.show as show

showcom = 'show ap database long'
#showcom = 'show ip dhcp binding'
#showcom = 'show ap debug log ap-name study-ap'

class NewAuth:
    def __init__(self, uidaruba, aos8ip, showcom):
        self.uidaruba = uidaruba
        self.aos8ip = aos8ip
        self.showcom = showcom

def readYaml():
    with open("data.yml", 'r') as ymlfile:
        data = yaml.load(ymlfile)
    return data

def get_new_token(aos8ip, username, password):
    tempauth = auth.AOS8Auth(aos8ip, username, password)
    tempsession = {}
    tempsession['uidaruba'] = tempauth.uidaruba

    with open(cookiefile, 'wt') as file:
        json.dump(tempsession, file)


def chksession(aos8ip, cookiefile):
    dtnow = datetime.datetime.now()
    now = time.mktime(dtnow.timetuple())
    timeout = 900

    # Try to get the filetime, if it fails assume it doesn't exist
    #  and move on to get a new token
    try:
        filetime = os.path.getmtime(cookiefile)
        difftime =  int(round(now - filetime))
    except:
        difftime = 1000

    if difftime > timeout:
        print('getting new token')
        get_new_token(aos8ip, username, password)
        print("refreshing token...")

# Read data from yaml file and set variables
data = readYaml()
username = data['user']
password = data['password']
controller_ip = data['controller_ip']
cookiefile = "aostoken-" + controller_ip + ".json"

# Get the cookie for the session
chksession(controller_ip, cookiefile)

# Open the session
with open(cookiefile) as tokenfile:
    tokenvar = json.load(tokenfile)
    token = tokenvar['uidaruba']
    session = NewAuth(token, controller_ip, showcom)

def convert_to_dhcp_table(session):
    import ast
    val = ast.literal_eval(json.dumps(show_bindings.show_bindings(session)))
    dhcptable = {}
    headers = "IP\t\tMAC\t\t\tStart\t\t\t\tEnd\t\t\t\tState"
    print(headers)
    for key, value in val.items():
        table ="{}\t{}\t{}\t{}\t{}".format(key, value['mac'], value['starts'], value['ends'], value['state'])
        print(table)
        #return table

def get_ap_mac_list(session):
    showapdata = json.loads(apdatabase.show_ap_database(session))
    for i in showapdata.items():
        # print("{} ".format(i["AP Database"]["AP Type"]))

        for k in range(len(i)):
            line = i[1][k]
            if line is not None:
                if isinstance(line, dict):
                    print("{} {} {}".format(line['AP Type'], line['IP Address'], line['Wired MAC Address']))

#getapmac = get_ap_mac_list(session)

#
# DHCP Binds
#
# def get_dhcppool(session):
#     pools = dhcppool.get_dhcppool(session)
#     print(json.dumps(pools))

# a = get_dhcppool(session)
# a = convert_to_dhcp_table(session)

#
# show ap database
#
print(json.dumps((apdatabase.show_ap_database(session))))
#print(json.dumps((show.show(session))))


#
# Dump session info
#
#print(json.dumps(show.show(session)))
# print(json.dumps(session.get_session))

#
# List containers
#
#print(json.dumps(container.get_container(session)))

#
# Parse DHCP Binds vi show command
#
# #print(dhcpbinds["_data"])
# for binds, value in dhcpbinds["_data"].items():
#     for lease in binds["_data"].items():
#         print(lease)
