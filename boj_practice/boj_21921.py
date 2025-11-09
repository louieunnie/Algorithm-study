import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split()) # N: 블로그 전체 일수, X: 기간

data = list(map(int, input().strip().split()))

window = sum(data[:M])
max_window = window
days = {window: 1}
for i in range(M, N):
    window = window + data[i] - data[i-M]
    if max_window < window:
        max_window = window
    if window in days:
        days[window] +=1
    else:
        days[window] = 1
if max_window == 0:
    print("SAD")
else:
    print(max_window)
    print(days[max_window])