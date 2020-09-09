#encoding:utf-8
import csv
from ping3 import ping, verbose_ping
ping.DEBUG = True

results = []

with open('surfshark_host.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        delay = ping(row[1],timeout=2,unit="ms")
        if not delay:
            print(f"{row[1]} delay ....")
            continue
        dic = {"host":row[0],"delay":delay}
        print(dic)
        results.append(dic)

ret = sorted(results,key=lambda item:item["delay"])

for i in range(10):
    print(ret[i])

