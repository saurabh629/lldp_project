'''
module :
    lldp_ios
description : 
    executed show lldp neighbor command and get list of dictionary of lldp neighbors
args :
    hostname
    username
    password
    host_connection
'''

import json
import requests

requests.packages.urllib3.disable_warnings()

def nxapi_call(show_command,hostname,username,password, port,content_type="json-rpc"):
    
    # Command NXAPI call
    url='http://%s:%s/ins' %(hostname, port)
    headers={'content-type' : 'application/%s' % content_type}
    payload = [
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
                "cmd": show_command,
                "version": 1.2
            },
            "id": 1
        }
    ]

    response=requests.post(url,
                            auth=(username,password),
                            headers=headers,
                            data=json.dumps(payload),
                            verify=False,
                            timeout=10)
    if response.status_code == 200:
        return response.json()
    else:
        msg = "call to %s failed, username %s password %s status_code %d" % (hostname, username, password, response.status_code)
        print msg
        raise Exception(msg)

def get_lldp_neighbor_list(hostname,username,password,host_connection):
    
    neighbor_list=[]
    neighbor_dict={}
    # getting output from show command via NXAPI4
    show_command = "show lldp neighbors"
    content_type = "json-rpc"
    http_port = 8080
    response = nxapi_call("show lldp neighbors",hostname,username,password,http_port)
    # creating list of lldp neighbor dictionaries
    listof_neighbors=response['result']['body']['TABLE_nbor']['ROW_nbor']
    for index,item in enumerate(listof_neighbors):
        neighbor_dict['neighbor_interface']=item['port_id']
        neighbor_dict['local_interface']=item['l_port_id']
        neighbor_dict['neighbor']=item['chassis_id']
        neighbor_list.append(neighbor_dict.copy())
    return neighbor_list