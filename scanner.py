#port scanner
#reconnasannce tool that scans a target and returns a list of open ports
#this gives information about the processes that may be running on the target
#industry standard is nmap


#we need to allow a user to specify a target
#make requests to every port
#return ports that are open

import sys
import socket
from datetime import datetime

target = input(str('Target IP:'))

print("Scanning Target: " + target)
print("Scan start time: " + str(datetime.now()))

try:
    for port in range(1, 10):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #socket.setdefaulttimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
        #s.close()
except KeyboardInterrupt:
    print("\n Exiting")
    sys.exit()

except socket.error:
    print("Host not responding")
    sys.exit()