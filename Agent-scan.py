import requests
import time
import json
import nmap
import threading


server_url = "http://localhost:3000"

def nmap_scan():
    pass

def get_request():
    while True:
        try:
            print("check")
            response = requests.get(server_url + "/agent-do")
            print(response.status_code)
            response = response.text
            # convert the text to dictionary
            response = json.loads(response)
            print(response)
            print(response['work'])
            # scan function
            if(response['work'] == 'scan'):
                # run scan function
                pass
            
        except Exception as e:
            print(f'{e}')
        time.sleep(1)     

get_thread = threading.Thread(target=get_request)
get_thread.start()

# other work

