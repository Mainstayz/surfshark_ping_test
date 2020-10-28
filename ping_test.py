# encoding:utf-8
import csv
from ping3 import ping, verbose_ping
import asyncio

ping.DEBUG = True

results = []


async def get_delay(host, ip):
    print(f"hello -> {host}")
    delay = ping(ip, timeout=2, unit="ms")
    if delay:
        print(f"{host} === {ip} ===> {delay} ms.")
    else:
        print(f"{host} === {ip} was timeout.")
    dic = {"host": host, "ip": ip, "delay": delay}
    return dic


tasks = []

with open("surfshark_host.csv") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    i = 1000
    for row in f_csv:
        future_task = asyncio.ensure_future(get_delay(row[0], row[1]))
        tasks.append(future_task)
        if len(tasks) > i:
            break

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

for task in tasks:
    result = task.result()
    if result["delay"]:
        results.append(result)

ret = sorted(results, key=lambda item: item["delay"])


print("\n\n go === >  https://bianyuan.xyz/ \n\n")

print("====== top 10! ======")

print(
    "vmess://ewogICJ2IjogIjIiLAogICJwcyI6ICJ3dWxhYmluZ19pb3Nlci5kZXYiLAogICJhZGQiOiAiaW9zZXIuZGV2IiwKICAicG9ydCI6ICI0NDMiLAogICJpZCI6ICJmOTNkYmU4My0xZDY2LTRmOWUtYWMwOC1lMTY1ZGQxODRjMGIiLAogICJhaWQiOiAiMiIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiAibm9uZSIsCiAgImhvc3QiOiAiaW9zZXIuZGV2IiwKICAicGF0aCI6ICIvODA1N2RmLyIsCiAgInRscyI6ICJ0bHMiCn0K"
)
for i in range(10):
    data = ret[i]
    name = data["host"].split(".")[0]
    msg = f"ss://YWVzLTI1Ni1nY206UFpucnBFbjZCNlJoUGc5SmdoVEFqYnlY@{data['ip']}:31300/?#{name}"
    print(msg)

