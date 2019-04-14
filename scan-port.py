#!/usr/bin/env python
# coding=utf-8

import sys
import socket

socket.setdefaulttimeout(0.5)

def scan(ip, port):
    print('Scaning %s:%s' % (ip, port))
    try:
        port = int(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((ip, port))
        if res == 0:
            print('[OPEN] %s:%s' % (ip, port))
        else:
            print('[CLOSE] %s:%s' % (ip, port))
        sock.close()
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting...')
    except socket.error:
        print('Can not connect to the server.')

if __name__ == '__main__':
    ip = sys.argv[1]
    port = sys.argv[2]
    scan(ip, port)
