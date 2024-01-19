import threading
from ping3 import ping
import time

def ping_ip(ip):
    while True:
        response = ping(ip)
        if response is not None:
            print(f"{ip} is reachable. Round-trip time: {response} ms")
        else:
            print(f"{ip} is not reachable.")

        # Wait for 1 minute before sending the next ping
        time.sleep(60)

def main():
    # List of IP addresses to ping
    ip_addresses = ['192.168.1.1', '192.168.1.2', '192.168.1.3']

    # Create a thread for each IP address
    threads = []
    for ip in ip_addresses:
        thread = threading.Thread(target=ping_ip, args=(ip,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
