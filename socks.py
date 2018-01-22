#!/usr/bin/env python3
import socket
iplist = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input("[*]Please enter the target machines IP address or domain address:")
def pscan(port):
    try:
        sock.connect((ip,port))
        return True
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        exit()
    except:
        return False
for x in range(3070,3074):
    if pscan(x):
        print('Port' ,x,'is open on this machine.')
    else:
        print('Port', x, 'is closed on this machine..')