# Function to get hardware info
function Get-HardwareInfo {
    $info = @{
        'cpu' = @{
            'name' = (Get-WmiObject Win32_Processor).Name
            'manufacturer' = (Get-WmiObject Win32_Processor).Manufacturer
            'architecture' = (Get-WmiObject Win32_Processor).AddressWidth
            'number_of_cores' = (Get-WmiObject Win32_Processor).NumberOfCores
            'number_of_logical_processors' = (Get-WmiObject Win32_Processor).NumberOfLogicalProcessors
        }
        'memory' = @{
            'total' = (Get-WmiObject Win32_ComputerSystem).TotalPhysicalMemory
            'free' = (Get-WmiObject Win32_OperatingSystem).FreePhysicalMemory
            'type' = (Get-WmiObject Win32_PhysicalMemory).MemoryType
            'speed' = (Get-WmiObject Win32_PhysicalMemory).Speed
        }
        'disk' = @{}
        'network' = Get-NetAdapter | ForEach-Object {
            $_.Name = $_.Name
            $_.MacAddress = $_.MacAddress
            $_
        }
    }
    
    Get-WmiObject Win32_DiskDrive | ForEach-Object {
        $info['disk'][$_.DeviceID] = @{
            'serial_number' = $_.SerialNumber
            'model' = $_.Model
            'size' = $_.Size
        }
    }

    $info['bios'] = @{
        'manufacturer' = (Get-WmiObject Win32_BIOS).Manufacturer
        'version' = (Get-WmiObject Win32_BIOS).Version
        'release_date' = (Get-WmiObject Win32_BIOS).ReleaseDate
    }

    $info['motherboard'] = @{
        'manufacturer' = (Get-WmiObject Win32_BaseBoard).Manufacturer
        'product' = (Get-WmiObject Win32_BaseBoard).Product
        'serial_number' = (Get-WmiObject Win32_BaseBoard).SerialNumber
    }

    $info['graphics'] = @{
        'name' = (Get-WmiObject Win32_VideoController).Name
        'adapter_ram' = (Get-WmiObject Win32_VideoController).AdapterRAM
        'driver_version' = (Get-WmiObject Win32_VideoController).DriverVersion
    }

    return $info
}

# Function to write info to file
function Write-InfoToFile {
    param (
        [Parameter(Mandatory=$true)]
        [Hashtable]$info,
        [Parameter(Mandatory=$true)]
        [string]$filename
    )
    $info | ConvertTo-Json | Out-File $filename
}

# Function to read info from file
function Read-InfoFromFile {
    param (
        [Parameter(Mandatory=$true)]
        [string]$filename
    )
    Get-Content $filename | ConvertFrom-Json
}

# Function to detect changes
function Detect-Changes {
    param (
        [Parameter(Mandatory=$true)]
        [Hashtable]$current_info,
        [Parameter(Mandatory=$true)]
        [Hashtable]$prev_info
    )
    $changes = @{}
    $current_info.GetEnumerator() | ForEach-Object {
        $key = $_.Key
        if ($current_info[$key] -ne $prev_info[$key]) {
            $changes[$key] = $current_info[$key]
        }
    }
    return $changes
}

# Main function
function Main {
    $filename = 'hardware_info.json'
    if (-not (Test-Path $filename)) {
        $current_info = Get-HardwareInfo
        Write-InfoToFile -info $current_info -filename $filename
    }
    else {
        $prev_info = Read-InfoFromFile -filename $filename
        $current_info = Get-HardwareInfo
        $current_hash = $current_info | Get-HashCode
        $prev_hash = $prev_info | Get-HashCode

        if ($current_hash -ne $prev_hash) {
            $changes = Detect-Changes -current_info $current_info -prev_info $prev_info
            $changes | ConvertTo-Json | Out-File 'changes.json'
        }
        Write-InfoToFile -info $current_info -filename $filename
    }
}

# Call Main function
Main
