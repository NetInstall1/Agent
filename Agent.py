import requests
import time
import json
import nmap
import threading
import socket
import subprocess
server_url = "http://localhost:5000"

# Create a config file that has ip_range that has to be scanned.
# Also create function that can edit the config file.



def psexec_command(ip_address, username, password, command):
    psexec_command_string  = f'psexec \\\\{ip_address} -s -u {username} -p {password} {command}'
    
    try:
        print("Executing psexec...")
        output = subprocess.check_output(psexec_command_string, 
        stderr=subprocess.STDOUT, shell=True, encoding='utf-8')
        print(output)
        return 1
    except subprocess.CalledProcessError as e:
        print("Error occured: " + str(e))
        

def get_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)
        print(f"The hostname for {ip_address} is {hostname[0]}")
        return hostname
    except socket.herror:
        print(f"Could not find the hostname for {ip_address}")
        return ''

def nmap_scan():

    
    target = "192.168.192.200" # This ip_range is for testing only.
    nm = nmap.PortScanner()
    print("Scanning...")
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
    return host_result

def login_into_guest(ip_address):
    print("Logging in...")
    with open('config.json', 'r') as f:
        general_info = json.load(f)
        print("config file content: " + str(general_info))
    username = general_info.get('username')
    password = general_info.get('password')
    command = 'cmd /c "echo Successful Login"'
    try:
        psexec_command(ip_address, username, password, command)
    except Exception as e:
        print("Error occurred in login: " + str(e))
def get_request():
    while True:
        try:
            print("sending get_request")
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
                # scan_result = json.dumps(scan_result)
                print("Scanned result\n" + str(scan_result))
                
                # post request to send the scan_result
                try:
                    headers = {'Content-Type': 'application/json'}
                    response = requests.post(server_url+"/scan_result", data= scan_result, headers= headers)
                    print(response)
                except Exception as e:
                    print("Post request failed "+ str(e))
            
            # After scan, login into each quest
            login_threads = []
            print(f"Length of scan_result: {len(scan_result)}")
            for guest in scan_result:
                print(guest)
                login_thread = threading.Thread(target=login_into_guest, args=(guest.get('ip_address'), ))
                login_threads.append(login_thread)
                login_thread.start()
            
            for login_thread in login_threads:
                login_thread.join()
            
        except Exception as e:
            print(f'{e}')
        time.sleep(1)     


get_thread = threading.Thread(target=get_request)
get_thread.start()

# other work



