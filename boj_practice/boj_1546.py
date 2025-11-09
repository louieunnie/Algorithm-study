import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))
greatest = max(data)
new_data = [d/greatest*100 for d in data]
new_avg = sum(new_data)/len(new_data)
print(round(new_avg, 4))
