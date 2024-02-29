import subprocess

async def psexec_command(ip_address, username, password, command):

    psexec_command_string  = f'psexec \\\\{ip_address} -s -u {username} -p {password} {command}'
    
    try:
        print("Executing psexec...")
        result = subprocess.check_output(psexec_command_string, shell=True, encoding='utf-8')
        # print(result)
        return result
        # if result.returncode == 0:
        #     # PsExec command succeeded
        #     print("PsExec command succeeded:")
        #     print(result.stdout)
        #     return result.stdout
        # else:
        #     # PsExec command failed
        #     print("PsExec command failed:")
        #     print(result.stderr)
        #     return result.stderr
    except subprocess.CalledProcessError as e:
        print("Error occured: " + str(e))