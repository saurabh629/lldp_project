'''This program can be used to get lldp neighbor information from various devices
    in a dictionary format
'''
# !/usr/bin/python
import json
import connect
import lldp_neighbor
import connect

def main():
    ''' main program to pass host details, connecting to device and getting
        lldp output information for the hosts in list of target_hosts
    '''
    # creating a list of target hosts for getting lldp neighbor details
    target_hosts = [("31.220.68.99", "ntc", "ntc123", "cisco_ios"),
                    ("31.220.70.252", "ntc", "ntc123", "cisco_ios"),
                    ("153.92.38.123", "ntc", "ntc123", "cisco_nxos"),
                    ("31.220.68.39", "ntc", "ntc123", "cisco_nxos"),]
    # creating a list of dictionaries with lldp neighbor details
    lldp_output = {}
    for (host, username, password, device_type) in target_hosts:
        host_connection = connect.get_device_connection(host, username, password, device_type)
        lldp_output[host] = lldp_neighbor.get_lldp_neighbor_list(host, username, password,
                                                                 host_connection, device_type)
    print json.dumps(lldp_output, indent=4, sort_keys=True)
if __name__ == '__main__':
    main()
