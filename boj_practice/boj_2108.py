import sys

input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

result = []
avg = sum(data)/len(data)
result.append(round(avg))

data.sort()
mid = data[len(data)//2]
result.append(mid)

from collections import Counter

ctr = Counter(data)
ctr = dict(ctr)
ctr = sorted(ctr.items(), key = lambda x: x[1])
most = max(list(x[1] for x in ctr))
rst = list(filter(lambda x: x[1] == most, ctr))
if len(rst) > 1:
    result.append(rst[1][0])
else:
    result.append(rst[0][0])
dif = data[-1]-data[0]
result.append(dif)
for r in result:
    print(r, end = "\n")