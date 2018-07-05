#!/usr/bin/env python3
import socket
import os
import sys
import argparse

os.system('clear')

class Scanner(object):
    def Args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-p","--port",help="[*]Use this option followed by the port you wish to punch", action='store',type=int)
        parser.add_argument("-t","--target",help="[*]Use this option followed by the port you wish to punch", action='store')
        args = parser.parse_args()
        port = args.port
        target = args.target
        if (port == None) | (target == None):
            print(parser.usage)
            exit(0)
        return port,target

    def ScanPort(self, port, target):
        socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data = bytes.fromhex('520500050106EF')

        try:
            socks.connect((target,int(port)))
            socks.settimeout(5)
            socks.sendall(data)
            print("[*] Port", port, "Is open!")

        except socket.error:
            print("[*]Port",port, "Is closed :(")
            sys.exit()
    
    
def main():
    target,port = Scanner().Args()
    Scanner().ScanPort(target,port)

main()

