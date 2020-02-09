from scapy.all import *

ip_layer = IP(dst='10.0.0.2')
icmp_layer = ICMP()
packet = ip_layer / icmp_layer
send(packet)