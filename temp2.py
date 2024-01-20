import json

# Provided input
input_str = """Caption                              DeviceID  MaxClockSpeed  Name                                    NumberOfCores
AMD64 Family 25 Model 80 Stepping 0  CPU0      2000           AMD Ryzen 7 5825U with Radeon Graphics  8

Capacity    DeviceLocator  Speed
8589934592  DIMM 0         3200
8589934592  DIMM 0         3200

Caption            DeviceID            Size
WD Blue SN570 1TB  \\.\PHYSICALDRIVE0  1000202273280


Windows IP Configuration

   Host Name . . . . . . . . . . . . : Kira
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No

Unknown adapter Local Area Connection 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Windscribe Windtun420
   Physical Address. . . . . . . . . :
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

Ethernet adapter Ethernet 2:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : VirtualBox Host-Only Ethernet Adapter
   Physical Address. . . . . . . . . : 0A-00-27-00-00-0E
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.56.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter Ethernet 4:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : VirtualBox Host-Only Ethernet Adapter #3
   Physical Address. . . . . . . . . : 0A-00-27-00-00-18
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::d9ff:72a4:ef26:dd1a%24(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.164.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 2047475751
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2B-62-AC-8B-00-0E-09-87-CD-81
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter Ethernet 3:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : VirtualBox Host-Only Ethernet Adapter #2
   Physical Address. . . . . . . . . : 0A-00-27-00-00-0C
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::e638:e8d4:c1ee:c31%12(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.1.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : -2113273817
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2B-62-AC-8B-00-0E-09-87-CD-81
   NetBIOS over Tcpip. . . . . . . . : Enabled

Unknown adapter Local Area Connection:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Windscribe VPN
   Physical Address. . . . . . . . . : 00-FF-BA-F1-6C-A3
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Unknown adapter Local Area Connection 3:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : TAP-Windows Adapter V9 for OpenVPN Connect
   Physical Address. . . . . . . . . : 00-FF-A9-5C-23-93
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Unknown adapter OpenVPN Connect DCO Adapter:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : OpenVPN Data Channel Offload
   Physical Address. . . . . . . . . :
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Local Area Connection* 13:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter #4
   Physical Address. . . . . . . . . : 3E-55-76-02-6D-29
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Local Area Connection* 17:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter #5
   Physical Address. . . . . . . . . : 3E-55-76-02-7D-39
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

Ethernet adapter ZeroTier One [e3918db483119a54]:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : ZeroTier Virtual Port
   Physical Address. . . . . . . . . : 56-3D-60-D2-8F-F9
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.192.26(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 25.255.255.254
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter ZeroTier One [48d6023c46e8899c]:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : ZeroTier Virtual Port #2
   Physical Address. . . . . . . . . : 9E-2E-99-17-07-76
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Autoconfiguration IPv4 Address. . : 169.254.145.132(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 25.255.255.254
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter ZeroTier One [856127940ce47d9c]:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : ZeroTier Virtual Port #3
   Physical Address. . . . . . . . . : 9E-DA-95-5D-AF-53
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::65bb:65c2:8545:8abc%6(Preferred)
   Autoconfiguration IPv4 Address. . : 169.254.233.57(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 25.255.255.254
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter ZeroTier One [e3918db48345542d]:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : ZeroTier Virtual Port #4
   Physical Address. . . . . . . . . : 2E-F3-34-D2-8F-F9
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::5047:3d38:1587:5c3a%35(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.147.18.26(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 25.255.255.254
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter ZeroTier One [272f5eae1688f49e]:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : ZeroTier Virtual Port #5
   Physical Address. . . . . . . . . : 9E-53-F9-47-95-2A
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::70ca:c017:904e:2045%9(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.22.143.107(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 25.255.255.254
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter ZeroTier One [60ee7c034a0e8ecd]:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : ZeroTier Virtual Port #7
   Physical Address. . . . . . . . . : CE-29-7F-1B-38-08
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::858a:1f3a:147a:f159%13(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.243.143.107(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 25.255.255.254
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter ZeroTier One [60ee7c034a8347f0]:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : ZeroTier Virtual Port #6
   Physical Address. . . . . . . . . : F2-E0-F2-1B-38-08
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::e25d:276a:9f5:7d95%30(Preferred)
   Autoconfiguration IPv4 Address. . : 169.254.200.244(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 25.255.255.254
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter ZeroTier One [60ee7c034af4b8d1]:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : ZeroTier Virtual Port #8
   Physical Address. . . . . . . . . : D2-1F-85-1B-38-08
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::8a3e:7c6f:29e2:b03b%133(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.147.17.26(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 25.255.255.254
   DHCPv6 IAID . . . . . . . . . . . : -2049826939
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2B-62-AC-8B-00-0E-09-87-CD-81
   NetBIOS over Tcpip. . . . . . . . : Enabled

Wireless LAN adapter Wi-Fi 2:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : MediaTek Wi-Fi 6 MT7921 Wireless LAN Card
   Physical Address. . . . . . . . . : 3C-55-76-02-4D-09
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.0.105(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : 19 January 2024 21:45:37
   Lease Expires . . . . . . . . . . : 21 January 2024 01:27:02
   Default Gateway . . . . . . . . . : 192.168.0.1
   DHCP Server . . . . . . . . . . . : 192.168.0.1
   DNS Servers . . . . . . . . . . . : 192.168.0.1
                                       0.0.0.0
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter vEthernet (Default Switch):

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter
   Physical Address. . . . . . . . . : 00-15-5D-08-C5-BE
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::47d1:ee45:6a4e:fc9e%97(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.23.96.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 1627395421
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2B-62-AC-8B-00-0E-09-87-CD-81
   NetBIOS over Tcpip. . . . . . . . : Enabled
Caption                   DeviceID          Name
AMD Radeon (TM) Graphics  VideoController1  AMD Radeon (TM) Graphics

OS Name:                   Microsoft Windows 11 Home Single Language"""

# Split the input into lines and extract values
lines = input_str.split('\n')
# header = lines[0].split()
print(lines[0])

# # print(header)
# output = []
# for i in range(1, len(lines)):
#     lines[i] = list(filter(None,lines[i].split("  ")))
#     item={}
#     item[header[0]]= lines[i][0]
#     item[header[1]]= lines[i][1]
#     item[header[2]]= lines[i][2]
#     # print(item)
#     output.append(item)

# print(output)



# output = {}
# print(values)

# Create a dictionary using the header and values
# output = {header[i]: values[i] for i in range(len(header))}

# Convert to JSON format
# json_output = json.dumps(output, indent=2)

# Print or save the JSON data
# print(json_output)


def string_function(*args):
    print(args)
    for string_arg in args:
        print(string_arg)

# Example call
string_function("Hello", "World", "Python", "Strings")