#port scanner
#reconnasannce tool that scans a target and returns a list of open ports
#this gives information about the processes that may be running on the target
#industry standard is nmap


#we need to allow a user to specify a target
#make requests to every port
#return ports that are open

import sys
import socket
import threading
import concurrent.futures
from datetime import datetime

target = input(str('Target IP:'))

print("Scanning Target: " + target)
print("Scan start time: " + str(datetime.now()))

def test_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        socket.setdefaulttimeout(1)
        print(f"Checking port {port}")
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")

try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for port in range(1, 1024):
            executor.map(test_port(port))

except KeyboardInterrupt:
    print("\n Exiting")
    sys.exit()

except socket.error:
    print("Host not responding")
    sys.exit()