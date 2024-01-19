import socket
import json
import nmap



def get_hostname(ip_address):
    try:
        print("Getting hostname...")
        hostname = socket.gethostbyaddr(ip_address)
        return hostname[0]
    except socket.herror:
        print(f"Could not find the hostname for {ip_address}")
        return ''

import socket
import platform

def get_os(ip_address):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip_address, 445))
        s.close()
        return platform.system()

    except socket.error:
        return ""

def get_agent_ip():
    print("Getting agent IP...")
    try:
        hostname = socket.gethostname()
        private_ip_address = socket.gethostbyname(hostname)
        return private_ip_address
    except Exception as e:
        print(f"Error while getting agent IP: {e}")
        return ''

    
def nmap_scan():

    with open('config.json', 'r') as f:
        config_file = json.load(f)
        target = config_file['ip_range'] # This ip_range is for testing only.
        print(f'Target IP range: {target}')
         
    try:
        nm = nmap.PortScanner()
        print(f"Scanning IP range: {target}")
        hosts = nm.scan(target, arguments="-sn -T5")
        host_results = []
        for ip_address, host_data in hosts['scan'].items():
            host = {
                "ip_address": ip_address,
                "hostname": host_data['hostnames'][0]['name'] if host_data.get('hostnames') else '',
                "mac_address": host_data.get('addresses', {}).get('mac', ''),
                "os": host_data['osmatch'][0]['name'] if host_data.get('osmatch') else '',
                "status": host_data.get('status', {}).get('state', ''),
                "action": "Discovered"
            }

            if not host['hostname']:
                host['hostname'] = get_hostname(host['ip_address'])

            print(f"Host info: {host}")
            host_results.append(host)

        return host_results
    except nmap.PortScannerError as e:
        print(f"Nmap scan error: {e}")
        return []