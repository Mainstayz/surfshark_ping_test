#encoding:utf-8
import csv
import fileinput
import sys
import re
import os

def replaceAll(file,pattern,subst):
    file_handle = open(file, 'r')
    file_string = file_handle.read()
    file_handle.close()
    file_string = (re.sub(pattern, subst, file_string))
    file_handle = open(file, 'w')
    file_handle.write(file_string)
    file_handle.close()



with open('surfshark_host.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        replaceAll(f"{row[0]}_udp.ovpn",f"remote .*? ",f"remote {row[1]} ")