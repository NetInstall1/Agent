from utils.psexec_util.psexec_process import *
import json
import asyncio
print("processor info")
# wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed

async def processor_info(ip_address, username, password):
    try:
        command = "wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed"
        result = psexec_command(ip_address, username, password, command)
        lines = result.split('\n')
        header = lines[0].split()
        values = list(filter(None, lines[1].split("  ")))
        output = {header[i]: values[i] for i in range(len(header))}
        json_output = json.dumps(output, indent=2)
        return json_output

    except Exception as e:
        print(f"Error occured in processor info: {e}")