from netmiko import ConnectHandler

def get_device_connection(hostname,username,password):
    
    # connecting to device
    connection_handle = ConnectHandler(
        device_type='cisco_nxos',
        ip=hostname,
        username=username,
        password=password,
        #secret='ntc123'
    )
    # enter enable mode
    connection_handle.enable()
    #output = connection_handle.send_command("show lldp neighbor")
    #re_table = textfsm.TextFSM(open("fsmtmp.textfsm"))
    #fsm_results = re_table.ParseText(output)
    #result  = parse_output(fsm_results)
    return connection_handle