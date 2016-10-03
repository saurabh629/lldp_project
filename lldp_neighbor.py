# !/usr/bin/python
import json
#import lldp_nxos
import connect

def main():
    #target_hosts = [("85.190.179.245","ntc","ntc123","nxos"),("153.92.38.174","ntc","ntc123","nxos")]
    target_hosts = [("153.92.39.183","ntc","ntc123","ios"),("85.190.179.150","ntc","ntc123","ios"),
    ("85.190.179.245","ntc","ntc123","nxos"),("153.92.38.174","ntc","ntc123","nxos")]
    lldp_output = {}
    for (host,username,password,os) in target_hosts:
    	if os == "nxos":
    		from lldp_nxos import get_lldp_neighbor_list
    	else:
    		from lldp_ios import get_lldp_neighbor_list
        host_connection = connect.get_device_connection(host,username,password)
        lldp_output[host]= get_lldp_neighbor_list(host,username,password,host_connection)
    print json.dumps(lldp_output,indent=4, sort_keys=True)
    print("finished successfully")

if __name__ == '__main__':
    main()