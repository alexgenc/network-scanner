# network scanner

import scapy.all as scapy
#from scapy.layers.l2 import Ether, ARP

def scan(ip_address):
    arp_request = scapy.ARP(pdst = ip_address)

    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout = 1)[0]

scan("192.168.0.1")