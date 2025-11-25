import socket
#if you are noticing the copy paste its cause i just set up the repo
def vulnScan(ip, ports): 
#takes in an ip and a list/range of ports 
# creates a list of open ports 
#open a socket that connects and then sends a exception to every port given 
#adds ports to a list that then gets return after for statement finishes 
    list = [] 
    for port in ports: 
        print("Testing port", port)
        test = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        if test.connect_ex((ip,port)) == 0: 
            print('THIS PORT IS OPEN') 
            list.append(port) 
        test.settimeout(.1) 
        test.close()
    return list


targetIP = '192.168.1.1'
# common open ports according to chatgpt
#[21,22,23,25,53,80,110,139,143,443,445,587,993,995,1433,1521,2049,3306,3389,5900,8000,8080,8443]
targetPorts = range(1,3) 
print('Starting Scan Now...')
vulnPorts = vulnScan(targetIP, targetPorts)
print("End of Scan \nOpen ports include:") 
if len(vulnPorts) == 0:
    print('There are no open ports')
else:
    for item in vulnPorts: 
        print(item)