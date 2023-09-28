import requests
import time
import json
import nmap
import threading
import socket

server_url = "http://localhost:5000"

# Create a config file that has ip_range that has to be scanned.
# Also create function that can edit the config file.

def get_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)
        print(f"The hostname for {ip_address} is {hostname[0]}")
        return hostname
    except socket.herror:
        print(f"Could not find the hostname for {ip_address}")
        return ''

def nmap_scan():

    target = "192.168.0.0-255" # This ip_range is for testing only.
    nm = nmap.PortScanner()

    hosts = nm.scan(target, arguments= "-sS -O")
    host_result = []
    for each_host in hosts['scan']:
        # [
        #     {   
        #         hostname,
        #         ip_address,
        #         mac_address,
        #         os_match,pa
        #         status
        #         Device type,
        #      },
        #       {...}
        # ]

        host = {
            "hostname": hosts['scan'][each_host]['hostnames'][0]['name'],
            "ip_address": each_host,
            "mac_address": hosts['scan'][each_host].get('addresses','').get('mac',''),
            "os": hosts['scan'][each_host]['osmatch'][0]['name'],
            "status": hosts['scan'][each_host].get('status','')['state'],
            "device_type": hosts['scan'][each_host]['hostnames'][0]['type']

        }
        host_result.append(host)
        print("Host: \n")
        print(host)
    return host_result
def get_request():
    while True:
        try:
            print("check")
            response = requests.get(server_url + "/api/agent-do")
            print(response.status_code)
            response = response.text

            # convert the text to dictionary
            response = json.loads(response)
            print(response)
            print(response['work'])

            # scan function
            if(response['work'] == 'scan'):
                scan_result = nmap_scan()
                scan_result = json.dumps(scan_result)
                print("Scanned result\n" + scan_result)
                # post request to send the scan_result
                try:
                    headers = {'Content-Type': 'application/json'}
                    response = requests.post(server_url+"/scan_result", data= scan_result, headers= headers)
                    print(response)
                except Exception as e:
                    print("Post request failed "+ str(e))
            
        except Exception as e:
            print(f'{e}')
        time.sleep(1)     


get_thread = threading.Thread(target=get_request)
get_thread.start()

# other work
def login():
    
    pass


