from collections import Counter
import sys
# print(ord("A")-ord('a')) -32

input = sys.stdin.readline

data = input().strip().lower()
ctr = dict(Counter(data))
values = [v for k, v in ctr.items()]
max_val = max(values)
most_ch = [k for k, v in ctr.items() if v == max_val]
if len(most_ch) >= 2:
    print("?")
else:
    print(most_ch[0].upper())