import json

# Provided input
input_str = """Capacity    DeviceLocator  Speed
8589934592  DIMM 0         3200
8589934592  DIMM 0         3200"""

# Split the input into lines and extract values
lines = input_str.split('\n')
header = lines[0].split()
# print(lines)

# print(header)
output = []
for i in range(1, len(lines)):
    lines[i] = list(filter(None,lines[i].split("  ")))
    item={}
    item[header[0]]= lines[i][0]
    item[header[1]]= lines[i][1]
    item[header[2]]= lines[i][2]
    # print(item)
    output.append(item)

print(output)



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