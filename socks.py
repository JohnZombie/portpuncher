#!/usr/bin/env python3
import socket
import os
os.system('clear')
ip = input("[*]Please enter the target machines IP address or domain address:")
socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portnum = int(input("[*]Please enter a port to scan:"))
data = bytes.fromhex('520500050106EF')
while True:
    try:
        socks.connect((ip,portnum))
        socks.settimeout(5)
        socks.send(data)
        print("**Port", portnum, "Is open..")
    except:
        print("**Port", portnum, "Is closed.")
    break


