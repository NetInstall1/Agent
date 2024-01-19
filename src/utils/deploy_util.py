import json
import threading
from utils.psexec_util.psexec_process import *
from nmap_util import *
import cloudinary
          
cloudinary.config( 
  cloud_name = "dwcx5qptc", 
  api_key = "118698334975328", 
  api_secret = "KNjj4cq1QSq4QdgdeSJt3ICqf1A" 
)

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
    # agent_ip_address = get_agent_ip()
    agent_ip_address = '10.147.18.26'
    quite_install_command = '/VERYSILENT /NORESTART /MERGETASKS=!runcode'
    netinstall_dir = 'C:/netinstall/software'
    # 
    filename = 'mongodb-windows-x86_64-7.0.1-signed.msi'
    filename2 = 'netinstallTest.txt'
    filename3 = 'python-3.9.0.exe'  
    filename4 = 'VSCodeSetup-x64-1.83.1.exe'
    # 

    deploy_threads = []
    for ip_address in ip_addresses:
        print("Deploy thread")
        command = fr'cmd /c "net use Z: \\{agent_ip_address}\netinstall /user:{username} {password} & copy Z:\{filename4} "{netinstall_dir}" & {netinstall_dir}/{filename4} {quite_install_command} & net use Z: /delete"'
        deploy_thread = threading.Thread(target=psexec_command, args=(ip_address, username, password, command, ))
        deploy_threads.append(deploy_thread)
        deploy_thread.start()
        # create a socket to update the status of the deploy-process.
    
    for deploy_thread in deploy_threads:
        deploy_thread.join()
    print("Deployed!")


deploy(['10.147.18.99', '10.147.18.139', '10.147.18.200'])