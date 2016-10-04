'''
module :
    lldp_neighbor
description : 
    invoke appropriate get_lldp_neighbor_list method based on router os 
args :
	hostname
	username
	password
    host_connection
    device_type
'''

import lldp_nxos
import lldp_ios

def get_lldp_neighbor_list(hostname,username,password,host_connection,device_type):
    
    if device_type == "cisco_nxos":
        result=lldp_nxos.get_lldp_neighbor_list(hostname,username,password,host_connection)
    else:
        result=lldp_ios.get_lldp_neighbor_list(hostname,username,password,host_connection)
    return result