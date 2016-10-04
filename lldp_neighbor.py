'''
module:
    connect
description:
    This module imports and calls appropriate method based on router os
'''
import lldp_nxos
import lldp_ios
def get_lldp_neighbor_list(hostname, username, password, host_connection, device_type):
    '''makes connection to device and return a connection handle
        kwargs:
            hostname
            username
            password
            device_type
    '''
    if device_type == "cisco_nxos":
        result = lldp_nxos.get_lldp_neighbor_list(hostname, username, password, host_connection)
    else:
        result = lldp_ios.get_lldp_neighbor_list(hostname, username, password, host_connection)
    return result
