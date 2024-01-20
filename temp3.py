import subprocess
import json
import re


command = 'echo processor info && wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed && echo processor info end && echo memory info && wmic memorychip get capacity, devicelocator, speed && echo memory info end && echo GPU info && wmic path win32_videocontroller get caption, deviceid, name && echo GPU info end && echo system info && systeminfo | find "OS Name" && echo system info end && echo network info && ipconfig /all && echo network info end && echo disk info && wmic diskdrive get caption, deviceid, size && echo disk info end'
# result = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)


# lines = result.stdout.split('\n')

result = '''processor info
Caption                               DeviceID  MaxClockSpeed  Name                            NumberOfCores
Intel64 Family 6 Model 79 Stepping 0  CPU0      2200           Intel(R) Xeon(R) CPU @ 2.20GHz  1

processor info end
memory info
Capacity    DeviceLocator  Speed
4294967296  DIMM 0         18756

memory info end
GPU info
No Instance(s) Available.


GPU info end
system info
OS Name:                   Microsoft Windows Server 2022 Datacenter
system info end
network info

Windows IP Configuration

   Host Name . . . . . . . . . . . . : guest1
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : asia-south1-c.c.divine-beach-411208.internal
                                       c.divine-beach-411208.internal
                                       google.internal

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : asia-south1-c.c.divine-beach-411208.internal.
   Description . . . . . . . . . . . : Google VirtIO Ethernet Adapter
   Physical Address. . . . . . . . . : 42-01-0A-A0-00-02
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::1205:2252:e9c7:8f4e%5(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.160.0.2(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Lease Obtained. . . . . . . . . . : Saturday, January 20, 2024 4:04:16 AM
   Lease Expires . . . . . . . . . . : Saturday, January 20, 2024 12:04:19 PM
   Default Gateway . . . . . . . . . : 10.160.0.1
   DHCP Server . . . . . . . . . . . : 169.254.169.254
   DHCPv6 IAID . . . . . . . . . . . : 104988938
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2D-38-4C-A3-42-01-0A-A0-00-02
   DNS Servers . . . . . . . . . . . : 10.160.0.1
   NetBIOS over Tcpip. . . . . . . . : Enabled
   Connection-specific DNS Suffix Search List :
                                       asia-south1-c.c.divine-beach-411208.internal
                                       c.divine-beach-411208.internal
                                       google.internal

Ethernet adapter ZeroTier One [60ee7c034a0e8ecd]:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : ZeroTier Virtual Port
   Physical Address. . . . . . . . . : CE-0C-70-04-04-9A
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::1aad:c060:8dfa:9ddf%9(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.243.130.212(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 25.255.255.254
   DNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1
                                       fec0:0:0:ffff::2%1
                                       fec0:0:0:ffff::3%1
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter ZeroTier One [48d6023c46889984]:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : ZeroTier Virtual Port #2
   Physical Address. . . . . . . . . : 86-1B-F6-08-3B-E4
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::2bb8:7649:23c8:8dac%8(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.22.130.212(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 25.255.255.254
   DNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1
                                       fec0:0:0:ffff::2%1
                                       fec0:0:0:ffff::3%1
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter ZeroTier One [56374ac9a4e4a27e]:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : ZeroTier Virtual Port #3
   Physical Address. . . . . . . . . : 7E-20-9A-EA-CE-AC
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::b7fc:dc83:b84:84bc%3(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.25.130.212(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 25.255.255.254
   DHCPv6 IAID . . . . . . . . . . . : 310255770
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2D-38-4C-A3-42-01-0A-A0-00-02
   DNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1
                                       fec0:0:0:ffff::2%1
                                       fec0:0:0:ffff::3%1
   NetBIOS over Tcpip. . . . . . . . : Enabled
network info end
disk info
Caption                                 DeviceID            Size
Google PersistentDisk SCSI Disk Device  \\.\PHYSICALDRIVE0  53686402560

disk info end'''

lines = result.split('\n')

in_processor_info = False
in_memory_info = False
in_gpu_info = False
in_system_info = False
in_network_info = False
in_disk_info = False

processor_info = {}
memory_info = []
gpu_info = {}
system_info = {}
network_info = {}
disk_info = {}

lines = [sublist for sublist in lines if sublist]
line_iter = iter(lines)

for line in line_iter:

    if line.strip() == "processor info":
        in_processor_info = True
        next_line = next(line_iter, None) # Move to the next line
        if next_line and next_line != "processor info end":
            header = list(filter(None,  re.split(r'\s+', next_line)))
        for line in line_iter:
            if not line.strip() or line.strip() == "processor info end":
                in_processor_info = False
                break
            values = list(filter(None, re.split(r'\s{2,}', line)))
            processor_info = {header[j]: values[j] for j in range(len(header))}
        # json_output = json.dumps(processor_info, indent=2)
        # print(json_output)
        

    elif line.strip() == "memory info":
        in_memory_info = True
        next_line = next(line_iter, None)  # Move to the next line
        if next_line and next_line != "memory info end":
            header = list(filter(None,  re.split(r'\s+', next_line)))
        for line in line_iter:
            if not line.strip() or line.strip() == "memory info end":
                in_memory_info = False
                break

            values = list(filter(None, re.split(r'\s{2,}', line)))
            memory_info.append({header[j]: values[j] for j in range(len(header))})
        # json_output = json.dumps(memory_info, indent=2)
        # print(json_output)

    elif line.strip() == "GPU info":
        in_gpu_info = True
        next_line = next(line_iter, None)  # Move to the next line
        if next_line and next_line != "GPU info end":
            header = list(filter(None, re.split(r'\s+', next_line)))
            print(next_line)
        for line in line_iter:
            print(line)
            if not line.strip() or line.strip() == "GPU info end":
                in_gpu_info = False
                break

            values = list(filter(None, re.split(r'\s{2,}', line)))
            gpu_info = {header[j]: values[j] for j in range(len(header))}
        # json_output = json.dumps(gpu_info, indent=2)
        # print(json_output)


    elif line.strip() == "system info":
        in_system_info = True
        next_line = next(line_iter, None)  # Move to the next line
        if next_line and next_line != "system info end":
            item = list(filter(None,  re.split(r'\s{2,}', next_line)))
            system_info = {item[0]: item[1]}
        # json_output = json.dumps(system_info, indent=2)
        # print(json_output)


    elif line.strip() == "network info":
        in_network_info = True
        key=''
        for line in line_iter:
            if not line.strip() or line.strip() == "network info end":
                in_network_info = False
                break
            if '.' not in line.strip():
                key = line.rstrip(':').strip()
                network_info[key] = {}
                line = next(line_iter, None)
            item = list(filter(None, line.split(":")))
            if len(item) > 1:
                network_info[key][item[0].replace('.', '').strip()] = item[1].strip() if item[1] else ''
        pretty_dict = json.dumps(network_info, indent=4)
        print(pretty_dict)

    elif line.strip() == "disk info":
        in_disk_info = True
        next_line = next(line_iter, None)  # Move to the next line
        if next_line and next_line != "disk info end":
            header = list(filter(None, re.split(r'\s+', line)))
        for line in line_iter:
            if not line.strip() or line.strip() == "disk info end":
                in_disk_info = False
                break
            values = list(filter(None, re.split(r'\s{2,}', line)))
            disk_info = {header[j]: values[j] for j in range(len(header))}
            print(disk_info)


# Organize the information into a dictionary
system_info_dict = {
    'Processor Information': processor_info,
    'Memory Information': memory_info,
    'GPU Information': gpu_info,
    'System Information': system_info,
    'Network Information': network_info,
    'Disk Information': disk_info
}

# Convert the dictionary to JSON
json_output = json.dumps(system_info_dict, indent=2)

# Print or use the JSON output as needed
print(json_output)
