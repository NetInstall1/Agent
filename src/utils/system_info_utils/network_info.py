import subprocess
import json
import re

def network_info():
    command = 'cmd /c "echo network info && ipconfig /all && echo network info end"'
    pass
command = 'echo processor info && wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed && echo processor info end && echo memory info && wmic memorychip get capacity, devicelocator, speed && echo memory info end && echo GPU info && wmic path win32_videocontroller get caption, deviceid, name && echo GPU info end && echo system info && systeminfo | find "OS Name" && echo system info end && echo network info && ipconfig /all && echo network info end && echo disk info && wmic diskdrive get caption, deviceid, size && echo disk info end'
result = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)

lines = result.stdout.split('\n')

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
        for line in line_iter:
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
# print(json_output)
