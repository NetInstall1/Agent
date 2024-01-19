import requests
import time
import json
import nmap
import threading
import socket
import subprocess
from utils.psexec_util.psexec_process import *
from utils.nmap_util import *
# import socketio
# import asyncio


# server_url = "http://localhost:5000"
server_url = None
# agent_id = '657d7ee9fbd88ba500b4fdfc'

# with open('config.json') as f:
#         server_url = json.load(f).get('server_url')
#         agent_id = json.load(f).get('agent_id')


# Socket io client setup
# sio = socketio.Client()

# @sio.event
# def connect():
#     print(f'Connected to server \nSocketId {sio.get_sid()}\nAgent id {agent_id}')
#     sio.emit('agent-connect', {'agent_id': agent_id, 'socket_id': sio.sid})



# @sio.event
# def connect_error():
#     print('error connecting to server')





def login_into_guest(ip_address):
    print("Logging in...")
    with open('config.json', 'r') as f:
        general_info = json.load(f)
        print("config file content: " + str(general_info))
    username = general_info.get('username')
    password = general_info.get('password')
    command = 'cmd /c "echo Successful Login"'
    # command = 'systeminfo'


    try:
        result = psexec_command(ip_address, username, password, command)
        print(result    )
        action = "Login Success"
        pass
    except Exception as e:
        print("Error occurred in login: " + str(e))
        action = "Login Failure"
    finally:
        login_result = {
            "ip_address": ip_address,
            "action": action,
            "details": result
        }
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(server_url + f"/api/agent-update-guest/{ip_address}", json=login_result, headers=headers)
    
        except Exception as post_exception:
            print(f"Error occurred during the guest-update POST request: {post_exception}")
        
    
    

def deploy(ip_addresses):
    print("Deploying...")
    # psexec \\192.168.192.200 -u netinstall -p n3tinst@ll -s cmd /c "net use Z: \\192.168.192.26\netinstall /user:netinstall n3tinst@ll & copy Z:\netinstallTest.txt "C:/netinstall/software" & net use Z: /delete"
    
    # Note: agent username and password must be same as other guests' username and password
    with open('config.json', 'r') as f:
        general_info = json.load(f)
        print("config file content: " + str(general_info))
    username = general_info.get('username')
    password = general_info.get('password')
    # command = 'cmd /c "net use Z: \\192.168.192.26\netinstall /user:netinstall n3tinst@ll & copy Z:\netinstallTest.txt "C:/netinstall/software" & net use Z: /delete'
    agent_ip_address = get_agent_ip()

    deploy_threads = []
    for ip_address in ip_addresses:
        command = f'cmd /c "net use Z: \\{agent_ip_address}\netinstall /user:{username} {password} & copy Z:\netinstallTest.txt "C:/netinstall/software" & net use Z: /delete'
        deploy_thread = threading.Thread(target=psexec_command, args=(ip_address, username, password, command, ))
        deploy_threads.append(deploy_thread)
        # create a socket to update the status of the deploy-process.



def get_request():
    while True:
        try:
            print("get_request sent")
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
                    response = requests.post(server_url+"/scan_result", json= scan_result, headers= headers)
                    print(response)
                except Exception as e:
                    print("Post request failed "+ str(e))
            
                # After scan, login into each quest
                login_threads = []
                print(f"Length of scan_result: {len(scan_result)}")
                print(f"Length: {scan_result}")
                for guest in scan_result:
                    print(guest)
                    login_thread = threading.Thread(target=login_into_guest, args=(guest.get('ip_address'), ))
                    login_threads.append(login_thread)
                    login_thread.start()

                print(f'login threads: {login_threads}')
                for login_thread_ in login_threads:
                    print(login_thread_)
                    login_thread_.join()
                print   ("Scan Complete!")

            elif(response['work'] == 'deploy'):
                ip_address = response['ip_address']
                deploy(ip_address)
            
        except Exception as e:
            try:
                headers = {'Content-Type': 'application/json'}
                response = requests.post(server_url+"/scan_result", json={"error":"Scan Error"}, headers= headers)
                print(response)
            except Exception as e:
                print("Post request failed "+ str(e))
            print(f'{e}')
        time.sleep(1)     



def main():
    get_thread = threading.Thread(target=get_request)
    get_thread.start()
    



if __name__ == "__main__":
    with open('config.json') as f:
        server_url = json.load(f).get('server_url')
        # agent_id = json.load(f).get('agent_id')
    # sio.connect(server_url)
    main()

