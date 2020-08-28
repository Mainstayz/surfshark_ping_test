#!Users/hezongzhu/.conda/envs/Zz/bin/python3
#encoding:utf-8
import csv
import socket

csvfile = csv.reader(open('surfshark.csv','r'))

rows = []
for row in csvfile:
    ip = socket.gethostbyname(row[2])
    if ip:
        dic = {'host':row[2],'ip':ip}
        rows.append(dic)
        print(f"write {dic}")


headers = ['host', 'ip']
with open('surfshark_host.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)