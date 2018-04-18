#!/usr/bin/env python3
import socket
import os
import sys

os.system('clear')

if len(sys.argv) != 3:
    print("Please type in an ip address then port. Ex: python3 socks.py 192.168.1.1 80")
    sys.exit(1)
ip = sys.argv[1]
port = sys.argv[2]
socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = bytes.fromhex('520500050106EF')

try:
    socks.connect((ip,int(port)))
    socks.settimeout(5)
    socks.sendall(data)
    print("[*] Port", port, "Is open!")

except socket.error:
    print("[*] Port", port, "Is closed....Sorry")
    sys.exit()




