import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as test:
    test.settimeout(1)
    name = socket.getservbyport(443)
    print(f"Service for port 443: {name}")
    print(name)