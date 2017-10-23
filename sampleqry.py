#!/usr/bin/env python3
import sys, json, requests, datetime, time, os, logging
import pprint

from pyaos8 import auth
import pyaos8.apdatabase as apdatabase
import pyaos8.show as show
import pyaos8.mactable as mactable
import pyaos8.container as container
#import pyaos8.session as session
import pyaos8.show_ip_dhcp_binding as show_bindings
import pyaos8.dhcp_pool as dhcppool
import pyaos8.show as show

username = 'admin'
password = 'Aruba123'
aos8ip = '10.0.1.5'
showcom = 'show ap database long'
#showcom = 'show ip dhcp binding'
# showcom = 'show ap debug log ap-name study-ap'
cookiefile = "aostoken-" + aos8ip + ".json"

def get_new_token(aos8ip, username, password):
    tempauth = auth.AOS8Auth(aos8ip, username, password)
    tempsession = {}
    tempsession['uidaruba'] = tempauth.uidaruba
    with open(cookiefile, "w") as f:
        json.dump(tempsession, f)


class NewAuth:
    def __init__(self, uidaruba, aos8ip, showcom):
        self.uidaruba = uidaruba
        self.aos8ip = aos8ip
        self.showcom = showcom


def chksession(aos8ip, cookiefile):
    dtnow = datetime.datetime.now()
    now = time.mktime(dtnow.timetuple())
    filetime = os.path.getmtime(cookiefile)
    difftime =  int(round(now - filetime))
    showcommand = "show web-server profile"
    # sessvar = NewAuth(token, aos8ip, showcommand)
    # json_data = json.loads(apdatabase.show_ap_database(sessvar))
    # for utimeout in json_data['Web Server Configuration']:
    #     if utimeout['Parameter'].startswith('User session'):
    #         timeout = float(utimeout['Value'])
    timeout = 900

    if difftime > timeout:
        get_new_token(aos8ip, username, password)
        print("refreshing token...")

chksession(aos8ip, cookiefile)

with open(cookiefile) as tokenfile:
    tokenvar = json.load(tokenfile)
    token = tokenvar['uidaruba']
    session = NewAuth(token, aos8ip, showcom)


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
#print(json.dumps((apdatabase.show_ap_database(session))))
#print(json.dumps((show.show(session))))


#
# Dump session info
#
#print(json.dumps(show.show(session)))
# print(json.dumps(session.get_session))

#
# List containers
#
print(json.dumps(container.get_container(session)))

#
# Parse DHCP Binds vi show command
#
# #print(dhcpbinds["_data"])
# for binds, value in dhcpbinds["_data"].items():
#     for lease in binds["_data"].items():
#         print(lease)
