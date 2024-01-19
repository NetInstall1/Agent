from utils.psexec_util.psexec_process import *
import json
import asyncio

print("memory info")
# wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed

async def memory_info(ip_address, username, password):
    try:
        command = "wmic memorychip get capacity, devicelocator, speed"
        result = psexec_command(ip_address, username, password, command)
        lines = result.split('\n')
        header = lines[0].split()
        output = []
        for i in range(1, len(lines)):
            lines[i] = list(filter(None,lines[i].split("  ")))
            item={}
            item[header[0]]= lines[i][0]
            item[header[1]]= lines[i][1]
            item[header[2]]= lines[i][2]
            output.append(item)
        json_output = json.dumps(output, indent=2)
        print(output)
        return json_output

    except Exception as e:
        print(f"Error occured in memory info: {e}")