#!/usr/bin/env python3
import socket

iplist = []
ip = input("[*]Please enter the target machines IP address or domain address:")
socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
prange = int(input("[*]Please enter a port to scan:"))
data = bytes.fromhex('520500050106EF')
while True:
    try:
        socks.connect((ip,prange))
        socks.settimeout(5)
        socks.send(data)
        print("Port", prange, "Is open..")
    except:
        print("Port", prange, "Is closed.")
    break


