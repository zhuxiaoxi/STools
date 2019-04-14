#!/usr/bin/env python
# coding=utf-8

import sys
from scapy.all import *


def scan(ip, port):
    print('Scaning %s:%s' % (ip, port))
    try:
        port = int(port)
        srcPort = RandShort()
        res = sr1(IP(dst=ip)/TCP(sport=srcPort, dport=port, flags="S"), timeout=10)
        if res.haslayer(TCP):
            if res.getlayer(TCP).flags == 'SA':
                sr(IP(dst=ip)/TCP(sport=srcPort, dport=port, flags="AR"), timeout=10)
                print('[OPEN] %s:%s' % (ip, port))
            elif res.getlayer(TCP).flags == 'RA':
                print('[CLOSE] %s:%s' % (ip, port))
    except:
        print('[ERROR] %s:%s' % (ip, port))
if __name__ == '__main__':
    ip = sys.argv[1]
    port = sys.argv[2]
    scan(ip, port)
