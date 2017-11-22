#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json
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

class pools():


    def get_ipv6_dhcp_excld_addr_cfg(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ipv6_dhcp_excld_addr_cfg?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ip_dhcp_excld_addr_cfg(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ip_dhcp_excld_addr_cfg?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_nat_pool(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "nat_pool?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ip_dhcp_adaptive(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ip_dhcp_adaptive?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_srv_dhcp_cfg(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "srv_dhcp_cfg?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ip_dhcp_opt82_web(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ip_dhcp_opt82_web?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ip_dhcp_dfl_pool_cfg(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ip_dhcp_dfl_pool_cfg?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ip_dhcp_pool_cfg(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ip_dhcp_pool_cfg?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_srv_dhcpv6_cfg(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "srv_dhcpv6_cfg?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_l2tp_local_pool_ipv6(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "l2tp_local_pool_ipv6?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ipv6_dhcp_pool_cfg(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ipv6_dhcp_pool_cfg?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ip_dhcp_opt82(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ip_dhcp_opt82?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_tun_pool(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "tun_pool?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_vlan_pool(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "vlan_pool?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_l2tp_local_pool(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "l2tp_local_pool?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ip_dhcp_lb_cfg(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ip_dhcp_lb_cfg?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_pptp_local_pool(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "pptp_local_pool?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ip_dhcp_ping_check_cfg(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ip_dhcp_ping_check_cfg?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response
