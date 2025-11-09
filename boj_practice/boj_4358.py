import sys

input = sys.stdin.readline
data = {}
total = 0
while True:
    name = input().strip()
    if name == '':
        break
    if name in data:
        data[name] += 1
    else:
        data[name] = 1
    total += 1

sorted_keys = sorted(list(data.keys()))
new_data = {}
for k in sorted(list(data.keys())):
    print(f"{k}{(data[k]/total*100): .4f}")