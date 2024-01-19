from utils.psexec_util.psexec_process import psexec_command
import asyncio

async def system_info(**kwargs):
    print("Hello")
    try:
        # command = "wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed &&  wmic memorychip get capacity, devicelocator, speed"

        # ip_address = kwargs.get("ip_address")
        # username = kwargs.get("username")
        # password = kwargs.get("password")

        # result = psexec_command(ip_address, username, password, command)
        # print(result)
        pass
    except Exception as e:
        print(f"Error occurred in system info: {e}")
    
