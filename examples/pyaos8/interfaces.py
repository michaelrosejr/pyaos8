import requests
import json
import sys

from requests.packages.urllib3.exceptions import InsecureRequestWarning
# from aosget import aosget

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def aosget(url, auth):
    aoscookie = dict(SESSION = auth.uidaruba)
    try:
        r = requests.get(url, cookies=aoscookie, verify=False)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Headers:', r.headers,
                  'Error Response:', r.reason)
        return r.text
    except requests.exceptions.RequestException as error:
        #print("Error")
        return "Error:\n" + str(error) + sys._getframe().f_code.co_name + ": An Error has occured"

def aosput(url, auth, payload):
    aoscookie = dict(SESSION = auth.uidaruba)
    try:
        r = requests.post(url, cookies=aoscookie, data=payload, verify=False)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Headers:', r.headers,
                  'Error Response:', r.reason)

        return r.text
    except requests.exceptions.RequestException as error:
        #print("Error")
        return "Error:\n" + str(error) + " get_interfaces: An Error has occured"

    url_write = "https://" + auth.aos8ip + ":4343/v1/configuration/object/write_memory?json=1&UIDARUBA=" + auth.uidaruba
    try:
        r = requests.post(url_write, cookies=aoscookie, verify=False)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Headers:', r.headers,
                  'Error Response:', r.reason)

        return r.text
    except requests.exceptions.RequestException as error:
        #print("Error")
        return "Error:\n" + str(error) + " url_write: An Error has occured"

class interfaces():


    def get_int_get(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/int_gig?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def vlan_id_get(auth):

        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/vlan_id?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response

    def vlan_id_post(auth, aosdata):
        aosdata = json.dumps(aosdata)
        print(aosdata)

        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/vlan_id?json=1&UIDARUBA=" + auth.uidaruba
        response = aosput(url, auth, aosdata)
        return response


    def get_int_mgmt(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "int_mgmt?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_rad_src_int(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "rad_src_int?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ipv6_gateway_ip(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ipv6_gateway_ip?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_stm_tun_node_addr(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "stm_tun_node_addr?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_int_pc(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "int_pc?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_tg(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "tg?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_int_range(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "int_range?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_rad_src_int_v6(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "rad_src_int_v6?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_int_gig(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "int_gig?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_int_cell(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "int_cell?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_vlan_id(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "vlan_id?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_int_tun(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "int_tun?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_stm_tun_node_mtu(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "stm_tun_node_mtu?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ip_flow_export_prof(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ip_flow_export_prof?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ping(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ping?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_rad_cp_redir_v6(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "rad_cp_redir_v6?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_int_loop(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "int_loop?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_stm_tun_loop_prevention(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "stm_tun_loop_prevention?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_vlan_range_rem(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "vlan_range_rem?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_vlan_name_id(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "vlan_name_id?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_rad_cp_redir(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "rad_cp_redir?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_int_vlan(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "int_vlan?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_vlan_range(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "vlan_range?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response
