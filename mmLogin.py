import requests
import pprint as pp
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# MM Login IP and credentials
userName = 'admin'
passWord = 'phattire'
deviceIP = '10.0.1.33'


values = {'username': userName,'password': passWord}
baseURL = "https://" + deviceIP + ":4343/v1"
loginURL = "https://" + deviceIP + ":4343/v1/api/login"
logoutURL = "https://" + deviceIP + ":4343/v1/api/logout"
#node_hierarchy = "https://10.3.3.233/v1/configuration/object/node_hierarchy"
node_hierarchy = baseURL + "/configuration/object/node_hierarchy"

def getCookie(authString):
    #print(authString)
    cookieString = str(authString)
    tmpList = cookieString.split(',')
    #print(tmpList[2])
    tmpStr = tmpList[2]
    tmpStr = tmpStr.replace('{','')
    tmpStr = tmpStr.replace('}','')
    tmpStr = tmpStr.replace('\"','')
    tmpStr = tmpStr.strip()
    print(tmpStr)
    tmpList = tmpStr.split(':')
    print(tmpList[1])
    return(tmpList[1])

with requests.Session() as query:
    #authentication login call
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    auth = query.post(loginURL, verify=False, data=values)
    #print (auth)
    #print("Request Content")
    #print(auth.content)
    #print("Cookie Jar")
    #print (auth.cookies)
    #print("Status code")
    #print(auth.status_code)

    ## Clean up cookie string and extract the Session ID
    UIDARUBA = getCookie(auth.content)
    node_hierarchy = node_hierarchy + '?UIDARUBA=' + UIDARUBA
    print(node_hierarchy)
    resp = query.get(node_hierarchy, cookies=auth.cookies,verify=False)
    print(resp.content.decode("utf-8"))

    print("Logging out of MM")
    auth = query.post(logoutURL, cookies=auth.cookies,verify=False)
    #print(auth)
    #print(auth.content)
    print(auth.status_code)
