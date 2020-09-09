import os
import sys
import socket
import csv

dir =  os.path.abspath(os.path.dirname(__file__))

tcp_arr = []
udp_arr = []

for _,_,files in os.walk(dir):
    for file in files:
        if (file.endswith("_tcp.ovpn")):
            tcp_arr.append(file)
        elif (file.endswith("_udp.ovpn")):
            udp_arr.append(file[0:-9])
            pass


for f in tcp_arr:
    if os.path.exists(f):
        os.remove(f)

rows = []
for f in udp_arr:
    ip = socket.gethostbyname(f)
    if ip:
        dic = {'host':f,'ip':ip}
        rows.append(dic)
        print(f"write {dic}")
    else:
        print(f"no {f} {ip}")


headers = ['host', 'ip']
with open('surfshark_host.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)




