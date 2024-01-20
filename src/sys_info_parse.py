import subprocess
import json
import re


def sys_info_parse(result):
    try:
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

        lines = [sublist.strip() for sublist in lines if sublist.strip()]
        line_iter = iter(lines)

        for line in line_iter:

            try:
                if line.strip() == "processor info":
                    in_processor_info = True
                    next_line = next(line_iter, None)  # Move to the next line
                    if next_line and next_line != "processor info end":
                        header = list(filter(None, re.split(r'\s+', next_line)))
                    for line in line_iter:
                        if not line.strip() or line.strip() == "processor info end":
                            in_processor_info = False
                            break
                        values = list(filter(None, re.split(r'\s{2,}', line)))
                        processor_info = {header[j]: values[j] for j in range(len(header))}
        

                elif line.strip() == "memory info":
                    in_memory_info = True
                    next_line = next(line_iter, None)  # Move to the next line
                    if next_line and next_line != "memory info end":
                        header = list(filter(None, re.split(r'\s+', next_line)))
                    for line in line_iter:
                        if not line.strip() or line.strip() == "memory info end":
                            in_memory_info = False
                            break

                        values = list(filter(None, re.split(r'\s{2,}', line)))
                        memory_info.append({header[j]: values[j] for j in range(len(header))})
        

                elif line.strip() == "GPU info":
                    in_gpu_info = True
                    next_line = next(line_iter, None)  # Move to the next line
                    print(next_line)
                    if next_line and next_line != "GPU info end":
                        header = list(filter(None, re.split(r'\s+', next_line)))
                        print(next_line)
                        print(header)
                        for line in line_iter:
                            print(line)
                            if not line.strip() or line.strip() == "GPU info end":
                                in_gpu_info = False
                                break
                            
                            values = list(filter(None, re.split(r'\s{2,}', line)))
                            gpu_info = {header[j]: values[j] for j in range(len(header))}
                        

                elif line.strip() == "system info":
                    in_system_info = True
                    next_line = next(line_iter, None)  # Move to the next line
                    if next_line and next_line != "system info end":
                        item = list(filter(None, re.split(r'\s{2,}', next_line)))
                        system_info = {item[0]: item[1]}
                    

                elif line.strip() == "network info":
                    in_network_info = True
                    key = ''
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
                        

            except IndexError as e:
                print(f"IndexError: {e}")
                raise ValueError("Index error occurred") from e
            except Exception as e:
                print(f"Unexpected error: {e}")
                # raise ValueError("Unexpected error occurred") from e

    except Exception as e:
        print(f"Outer Unexpected error: {e}")
        raise ValueError("Outer unexpected error occurred") from e

    # Organize the information into a dictionary
    system_info_dict = {
        'Processor Information': processor_info,
        'Memory Information': memory_info,
        'GPU Information': gpu_info,
        'System Information': system_info,
        'Network Information': network_info,
        'Disk Information': disk_info
    }

    print("in parse")
    print(system_info_dict)
    return system_info_dict
