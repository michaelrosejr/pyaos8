#!/usr/bin/env python3
import sys, json, requests, datetime, time, os, logging
import pprint

from pyaos8 import auth
import pyaos8.apdatabase as apdatabase
#import pyaos8.session as session

username = 'admin'
password = 'phattire'
aos8ip = '10.0.1.5'
showcom = 'show ap database long'
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




#print("uidaruba", token['uidaruba'])
#print("UIDARUBA: ", token)
# print(json.dumps(session.get_session))

#print(json.dumps((apdatabase.show_ap_database())))
print(apdatabase.show_ap_database(session))
