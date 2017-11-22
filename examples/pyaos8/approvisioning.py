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

class approvisioning():


    def get_prov_ap_reprovision(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "prov_ap_reprovision?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_apflash(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "apflash?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_wdb_rap_del(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "wdb_rap_del?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_prov_ap_set_trust_anchor(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "prov_ap_set_trust_anchor?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_disable_whitelist_sync(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "disable_whitelist_sync?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_leds(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_leds?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_copy_provisioning_params(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "copy_provisioning_params?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_image_preload_clear_group(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_image_preload_clear_group?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_image_preload_clear_name(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_image_preload_clear_name?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_set_trust_anchor(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "set_trust_anchor?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_reprovision(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_reprovision?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_prov(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_prov?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_prov_ap_reset_bootinfo(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "prov_ap_reset_bootinfo?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_apmove_ap(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "apmove_ap?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_reprovision(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "reprovision?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_sapm_gapdb_resync(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "sapm_gapdb_resync?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_set_ikepsk_by_addr(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "set_ikepsk_by_addr?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_consolidated_provision(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_consolidated_provision?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_apmove_all_ap(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "apmove_all_ap?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_image_preload_cancel(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_image_preload_cancel?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_ugr_mov(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_ugr_mov?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_clr_gapdb_ap_lms(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "clr_gapdb_ap_lms?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_regroup(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_regroup?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_provisioning_prof(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_provisioning_prof?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_prov_ap_set_ikepsk_by_addr(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "prov_ap_set_ikepsk_by_addr?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_mesh_recovery_profile(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "mesh_recovery_profile?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_sapm_test_airmatch_disallow_act(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "sapm_test_airmatch_disallow_act?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_wdb_cpsec_add_mac(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "wdb_cpsec_add_mac?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_sapm_test_airmatch_allow_act(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "sapm_test_airmatch_allow_act?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_clear_ap_port(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "clear_ap_port?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_prov_ap_read_bootinfo(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "prov_ap_read_bootinfo?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_wdb_cpsec_modify_mac(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "wdb_cpsec_modify_mac?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_sapm_gapdb_reinit_db(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "sapm_gapdb_reinit_db?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_wdb_rap_modify(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "wdb_rap_modify?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_image_preload(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_image_preload?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_ugr_add(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_ugr_add?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_read_bootinfo(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "read_bootinfo?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_wdb_rap_add(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "wdb_rap_add?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_apboot(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "apboot?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_wdb_purge(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "wdb_purge?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_prov_ap_copy_provision_params(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "prov_ap_copy_provision_params?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_apconnect(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "apconnect?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_image_preload_group(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_image_preload_group?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_wdb_cpsec_revoke_mac(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "wdb_cpsec_revoke_mac?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_image_preload_name(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_image_preload_name?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_ugr_act(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_ugr_act?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_multizone_whitelist_export(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_multizone_whitelist_export?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_apdisconnect(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "apdisconnect?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_image_preload_clear_all(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_image_preload_clear_all?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_sapm_gapdb_resync_v6(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "sapm_gapdb_resync_v6?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_sapm_test_wan_uplink(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "sapm_test_wan_uplink?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_sapm_test_wan_down(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "sapm_test_wan_down?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_reset_bootinfo(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "reset_bootinfo?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_wdb_cpsec_del_mac(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "wdb_cpsec_del_mac?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_rename(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_rename?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_export_gapdb(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "export_gapdb?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_wdb_rap_revoke(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "wdb_rap_revoke?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response


    def get_ap_testcmd(auth):
        url = "https://" + auth.aos8ip + ":4343/v1/configuration/object/" \
              "ap_testcmd?json=1&UIDARUBA=" + auth.uidaruba
        response = aosget(url, auth)
        return response
