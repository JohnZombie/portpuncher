#!/usr/bin/env python3
import socket
import os
import sys

os.system('clear')

class Cli(object):
    def args(self):
        try:
            ip = sys.argv[1]
            port = sys.argv[2]
        except:
            print("Please type in an ip address then port. Ex: python3 socks.py 192.168.1.1 80")
            sys.exit(1)
        return ip,port    
    def scan(self, host , port):
        socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data = bytes.fromhex('520500050106EF')
        while True:
            try:
                socks.connect((ip,port))
                socks.settimeout(5)
                socks.send(data)
                print("**Port", port, "Is open..")
            except:
                print("**Port", port, "Is closed.")
            break


ip, port = Cli().args()

print("Now Scanning:",ip,port)

Cli().scan(ip, port)

