# !/usr/bin/python

import json
import requests
import jtextfsm as textfsm

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

def get_lldp_neighbor_list(hostname,username,password,connection_handle):
    
    neighbor_list=[]
    neighbor_dict={}
    # getting output from show command via NXAPI4
    show_command = "show lldp neighbors"
    content_type = "json-rpc"
    http_port = 8080
    response = nxapi_call("show lldp neighbors",hostname,username,password,http_port)
    # creating list of lldp neighbor dictionaries
    numof_intf=len(response['result']['body']['TABLE_nbor']['ROW_nbor'])
    for index in range(numof_intf):
        neighbor_dict['neighbor_interface']=response['result']['body']['TABLE_nbor']['ROW_nbor'][index]['port_id']
        neighbor_dict['local_interface']=response['result']['body']['TABLE_nbor']['ROW_nbor'][index]['l_port_id']
        neighbor_dict['neighbor']=response['result']['body']['TABLE_nbor']['ROW_nbor'][index]['chassis_id']
        neighbor_list.append(neighbor_dict.copy())
    #result_output[hosts]=lldp_neighbor_list
    #print json.dumps(result_output, indent=4, sort_keys=True)
    #return result_output
    return neighbor_list