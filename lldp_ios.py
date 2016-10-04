'''
module:
    lldp_ios
description:
    This module groups methods for running lldp commands on ios device
'''
import jtextfsm as textfsm

def get_lldp_neighbor_list(hostname, username, password, host_connection):
    '''executes show lldp neighbor command and get list of dictionary of lldp neighbors
    kwargs:
        hostname
        username
        password
        host_connection
    '''
    neighbor_list = []
    neighbor_dict = {}
    # getting output from show command
    output = host_connection.send_command("show lldp neighbor")
    # parsing output through fsmtext
    re_table = textfsm.TextFSM(open("lldp.textfsm"))
    fsm_result = re_table.ParseText(output)
    # creating list of dictionary of lldp neighbors
    for index_of_fsm, list_of_list in enumerate(fsm_result):
        if index_of_fsm == 0:
            for index, item in enumerate(list_of_list):
                if "Device ID" in item:
                    device_index = index
                if  "Local Intf" in item:
                    localp_index = index
                if "Port ID" in item:
                    port_index = index
        else:
            neighbor_dict['neighbor_interface'] = fsm_result[index_of_fsm][port_index]
            neighbor_dict['local_interface'] = fsm_result[index_of_fsm][localp_index]
            neighbor_dict['neighbor'] = fsm_result[index_of_fsm][device_index]
            neighbor_list.append(neighbor_dict.copy())
    return neighbor_list
