from utils.psexec_util.psexec_process import psexec_command
from sys_info_parse import *

import asyncio

async def system_info(**kwargs):
    try:
        command = 'cmd /c "echo processor info && wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed && echo processor info end && echo memory info && wmic memorychip get capacity, devicelocator, speed && echo memory info end && echo GPU info && wmic path win32_videocontroller get caption, deviceid, name && echo GPU info end && echo system info && systeminfo | find "OS Name" && echo system info end && echo network info && ipconfig /all && echo network info end && echo disk info && wmic diskdrive get caption, deviceid, size && echo disk info end"'

        ip_address = kwargs.get("ip_address")
        username = kwargs.get("username")
        password = kwargs.get("password")

        result = await psexec_command(ip_address, username, password, command)

        # print(result)
        # Parse the result
        result = sys_info_parse(result)
        return result
    except Exception as e:
        print(f"Error occurred in system info: {e}")
    
