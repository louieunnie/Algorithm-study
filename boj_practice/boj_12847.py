import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
T = list(map(int, input().strip().split()))

window = sum(T[:m])
max_profit = window

for i in range(m, n):
    window = window + T[i] - T[i-m]
    if window > max_profit:
        max_profit = window
    
print(max_profit)