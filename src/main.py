import requests
import time
import json
import nmap
import threading
import socket
import subprocess
from utils.psexec_util.psexec_process import *
from utils.system_info_utils.system_info_com import system_info
from utils.nmap_util import *
from concurrent.futures import ThreadPoolExecutor
# import socketio
import asyncio
import os
import shutil

# server_url = "http://localhost:5000"
server_url = None
# agent_id = '657d7ee9fbd88ba500b4fdfc'


def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


async def login_into_guest(ip_address):
    print("Logging in...")
    with open('config.json', 'r') as f:
        general_info = json.load(f)
        print("config file content: " + str(general_info))
    username = general_info.get('username')
    password = general_info.get('password')
    command = 'cmd /c "echo Successful Login"'
    # command = 'systeminfo'
    
    system_task = asyncio.create_task(system_info(ip_address=ip_address, username=username, password=password))

    try:
        result = await psexec_command(ip_address, username, password, command)
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

        sys_info = await system_task
        print('Sys')
        print(sys_info)
        try:
            print(ip_address)
            response = requests.post(server_url + f"/api/guest-sys-info/{ip_address}", json=sys_info, headers=headers)
            print(response)
        except Exception as post_exception:
            print(f"Error occurred during the guest-update POST request: {post_exception}")
        

def run_psexec_command(ip_address, username, password, command):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(psexec_command(ip_address, username, password, command))


def download_file(file_path, dest_folder):
    # Check if the file_path is a URL or a local file path
    if file_path.startswith(('http://', 'https://')):
        # Handle the URL case with requests
        local_filename = os.path.join(dest_folder, file_path.split('/')[-1])
        with requests.get(file_path, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
    else:
        # Handle the local file path case with shutil
        local_filename = os.path.join(dest_folder, os.path.basename(file_path))
        shutil.copyfile(file_path, local_filename)
    return local_filename

def check_for_new_uploads(server_url, destination_folder):
    while True:
        try:
            response = requests.get(server_url + '/api/new-uploads')
            if response.status_code == 200:
                uploads = response.json()
                for upload in uploads:
                    file_url = upload['filePath']  # Assuming this is a direct URL to download the file
                    download_file(file_url, destination_folder)
                    print(f"Downloaded {upload['softwareName']} to {destination_folder}")
        except Exception as e:
            print(f"Error checking for new uploads: {e}")
        time.sleep(10)



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



async def get_request():
    while True:
        try:
            print("get_request sent")
            response = requests.get(server_url + "/api/agent-do")
            print(response.status_code)
            response = response.text
            response = json.loads(response)
            print(response)
            print(response['work'])

            # scan function
            if(response['work'] == 'scan'):
                scan_result = await nmap_scan()
                
                # post request to send the scan_result
                try:
                    headers = {'Content-Type': 'application/json'}
                    response = requests.post(server_url+"/scan_result", json= scan_result, headers= headers)
                    # print(response)
                except Exception as e:
                    print("Post request failed "+ str(e))
            
                # After scan, login into each quest
                login_tasks = []
                # print(f"Length: {scan_result}")
                for guest in scan_result:
                    print(guest)
                    login_task = asyncio.create_task(login_into_guest(guest.get('ip_address')))
                    login_tasks.append(login_task)

                await asyncio.gather(*login_tasks)


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
                # print(f'{e}')
        time.sleep(1)     



async def main():
    global server_url  # Declare server_url as global to modify the global variable
    global username
    global password
    global agent_ip_address
    with open('config.json') as f:
        config = json.load(f)
        server_url = config.get('server_url')
        username = config.get('username')
        password = config.get('password')
        agent_ip_address = config.get('agent_ip_address')

        if not server_url:  # Check if server_url is not None or empty
            raise ValueError("server_url not found in config.json")
    with ThreadPoolExecutor() as executor:
        with open('config.json') as f:
            server_url = json.load(f).get('server_url')
        destination_folder = 'C:/netinstall/software'
        # destination_folder = os.path.join(os.path.dirname(), 'Files')
        ensure_directory_exists(destination_folder)
        executor.submit(check_for_new_uploads, server_url, destination_folder)
        await asyncio.gather(get_request())
    

if __name__ == "__main__":
        # agent_id = json.load(f).get('agent_id')
    # sio.connect(server_url)
    asyncio.run(main())

