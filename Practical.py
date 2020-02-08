#!/bin/python3
import os
import logging
import subprocess
attack1 = 'Attack1.py'
while True:
    attack = int(input('Choose Attack:  '))

    
    if attack <2:
        print("SYN Scan")
        subprocess.call('Attack1.py', shell=True)
    else:
        print('This is Not An Attack')
print('YOU GET A ZEROOOO')