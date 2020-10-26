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
            print(f"{row[0]} {row[1]} delay ....")
            continue
        dic = {"host":row[0],"ip":row[1],"delay":delay}
        print(dic)
        results.append(dic)

ret = sorted(results,key=lambda item:item["delay"])

print("====== top 10! ======")
print("https://bianyuan.xyz/")
# ss://method:password@server:port
# ss://YWVzLTI1Ni1nY206UFpucnBFbjZCNlJoUGc5SmdoVEFqYnlY@198.8.80.83:31300/?#us-sea
# ss://YWVzLTI1Ni1nY206UFpucnBFbjZCNlJoUGc5SmdoVEFqYnlY@95.174.65.71:31300/?#dk-cph

print("vmess://ewogICJ2IjogIjIiLAogICJwcyI6ICJ3dWxhYmluZ19pb3Nlci5kZXYiLAogICJhZGQiOiAiaW9zZXIuZGV2IiwKICAicG9ydCI6ICI0NDMiLAogICJpZCI6ICJmOTNkYmU4My0xZDY2LTRmOWUtYWMwOC1lMTY1ZGQxODRjMGIiLAogICJhaWQiOiAiMiIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiAibm9uZSIsCiAgImhvc3QiOiAiaW9zZXIuZGV2IiwKICAicGF0aCI6ICIvODA1N2RmLyIsCiAgInRscyI6ICJ0bHMiCn0K")
for i in range(10):
    data = ret[i]
    name = data['host'].split('.')[0]
    msg = f"ss://YWVzLTI1Ni1nY206UFpucnBFbjZCNlJoUGc5SmdoVEFqYnlY@{data['ip']}:31300/?#{name}"
    print(msg)

