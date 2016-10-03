import json
import jtextfsm as textfsm


def get_device_connection(hostname,username,password):
    
    # connecting to device
    connection_handle = ConnectHandler(
        device_type='cisco_ios',
        ip=hostname,
        username=username,
        password=password,
        secret='ntc123'
    )
    # enter enable mode
    connection_handle.enable()
    return connection_handle
        
def get_lldp_neighbor_list(hostname,username,password,connection_handle):
    
    neighbor_list=[]
    neighbor_dict={}
    # getting output from show command
    output = connection_handle.send_command("show lldp neighbor")
    # parsing output through fsmtext
    re_table = textfsm.TextFSM(open("lldp.textfsm"))
    fsm_result = re_table.ParseText(output)
    #fsm_result_list = parse_output(fsm_result)
    
    numof_neighbors=len(fsm_result)
    for index in range(1,numof_neighbors):
        neighbor_dict['neighbor_interface']=fsm_result[index][4]
        neighbor_dict['local_interface']=fsm_result[index][1]
        neighbor_dict['neighbor']=fsm_result[index][0]
        neighbor_list.append(neighbor_dict.copy())
    return neighbor_list

