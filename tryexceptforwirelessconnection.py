try:  
        if test.connect_ex((192.168.1.219:139)) == 0:
            message = "packets"
            test.sendall(message.encode('utf-8'))
            info = test.recv(4096)
            print(f'Recieved:{info.decode()}')
    except ConnectionRefusedError:
        print('Actively Refused (Port Closed)')
    except socket.timeout:
        print('Port is filtered/unresponsive')
    except OSError:
        print('Port is unreachable')