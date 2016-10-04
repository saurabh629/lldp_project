'''
module :
    connect
description : 
    makes connection to device and return a connection handle 
args :
    hostname
    username
    password
    device_type
'''
from netmiko import ConnectHandler
    
def get_device_connection(hostname,username,password,device_type):
    
    # connecting to device
    connection_handle = ConnectHandler(
        device_type=device_type,
        ip=hostname,
        username=username,
        password=password,
    )
    # enter enable mode
    connection_handle.enable()
    return connection_handle