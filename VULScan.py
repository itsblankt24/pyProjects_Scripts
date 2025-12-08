import socket
import sys
#if you are noticing the copy paste its cause i just set up the repo
def vulnScan(ip, ports): 
#takes in an ip and a list/range of ports 
# creates a list of open ports 
#open a socket that connects and then sends a exception to every port given 
#adds ports to a list that then gets return after for statement finishes 
    VPorts = [] 
    for port in ports:
        sys.stdout.write(f'\rScanning Port {port}')
        #print('Scanning Port', port)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as p:
            p.settimeout(.5)
            if p.connect_ex((ip,port)) == 0:
                VPorts.append(port) 
        sys.stdout.flush
    return VPorts 
def getPrintScan(targetIP, targetPorts):
    print('Starting Scan Now...')
    vulnPorts = vulnScan(targetIP, targetPorts)
    print("\nEnd of Scan \nOpen ports include:") 
    if len(vulnPorts) == 0:
        print('There are no open ports')
    else:
        for x in vulnPorts: 
            print('\nport:', x)
            name = socket.getservbyport(x)
            print('protocol:', name)


# common open ports according to chatgpt
targetPorts = [21,22,23,25,53,80,110,139,143,443,445,587,993,995,1433,1521,2049,3306,3389,5900,8000,8080,8443]
#targetPorts = range(4800,5200) 
targetIP = '192.168.1.1'
getPrintScan(targetIP, targetPorts)



# ============ According to Chat GPT ============
# ===== Future Enhancements for Port Scanner =====
# 1. Add banner grabbing:
#    - After detecting an open port, attempt to read the service banner
#    - Helps identify the service and version (e.g., Apache 2.4.49, OpenSSH 7.9)
#
# 2. Implement port-to-service mapping:
#    - Convert port numbers to service names (e.g., 80 -> HTTP, 22 -> SSH)
#
# 3. Add threading (multi-threading or asyncio):
#    - Speed up scanning significantly by testing multiple ports in parallel
#
# 4. Include risk analysis:
#    - Tag ports as Low, Medium, High, or Critical risk based on service
#
# 5. Create formatted scan reports:
#    - Export results to text, CSV, JSON, or HTML report formats
#
# 6. Add command-line interface (CLI):
#    - Allow running the scanner using command-line arguments
#      Example: python scanner.py --ip 192.168.1.10 --ports common
#
# 7. Add UDP scanning support (optional and more advanced)
#    - Use sockets or scapy to detect UDP-based services (DNS, SNMP, DHCP)
#
# 8. Integrate vulnerability lookup:
#    - Match detected service versions to real CVEs using local database or API
#
# 9. Improve handling of unreachable hosts and exceptions
#
# 10. Build a Flask or web-based dashboard (long-term goal)
