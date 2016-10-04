# !/usr/bin/python
import json
import connect
from lldp_neighbor import *
from connect import *

def main():
    # creating a list of target hosts for getting lldp neighbor details
    target_hosts= [("31.220.71.10","ntc","ntc123","cisco_ios"),("31.220.69.146","ntc","ntc123","cisco_ios"),
                  ("153.92.37.150","ntc","ntc123","cisco_nxos"),("153.92.38.209","ntc","ntc123","cisco_nxos"),]
    # creating a list of dictionaries with lldp neighbor details
    lldp_output = {}
    for (host,username,password,device_type) in target_hosts:
        host_connection = get_device_connection(host,username,password,device_type)
        lldp_output[host]= get_lldp_neighbor_list(host,username,password,host_connection,device_type)
    print json.dumps(lldp_output,indent=4, sort_keys=True)
    print("finished successfully")

if __name__ == '__main__':
    main()