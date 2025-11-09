import sys

input = sys.stdin.readline

N, K = map(int, input().strip().split())
data = list(map(int, input().strip().split()))

cons = []
window = sum(data[:K])
max = window
# print(first)m
# print(total)
for i in range(K, N):
    window = window -data[i-K] +data[i]
    if max < window:
        max = window
    # print(window)
    
print(max)