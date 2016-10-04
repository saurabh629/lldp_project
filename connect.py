'''
module:
    connect
description:
    This module groups methods for device connection
'''
from netmiko import ConnectHandler

def get_device_connection(hostname, username, password, device_type):
    '''makes connection to device and return a connection handle
        kwargs:
            hostname
            username
            password
            device_type
    '''
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
