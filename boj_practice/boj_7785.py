## 집합 쓰기!!

import sys

input = sys.stdin.readline

N = int(input()) # 사람의 수

now = set()
for _ in range(N):
    name, status = input().strip().split()
    if status == "enter":
        now.add(name)
    elif status == "leave":
        now.remove(name)
if len(now) == 0:
    print("")
else:
    now = sorted(now, reverse = True)
    for name in now:
        print(name)