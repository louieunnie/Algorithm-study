import sys

input = sys.stdin.readline

K = int(input())

def stat(N, arr):
    result = []
    result.append(max(arr))
    result.append(min(arr))
    largest_gap = 0
    arr = sorted(arr)
    for i in range(N-1):
        gap = arr[i+1]-arr[i]
        if gap >= largest_gap:
            largest_gap = gap
    result.append(largest_gap)
    return result


for i in range(1, K+1):
    data = list(map(int, input().split()))
    N = data[0]
    data = data[1:]
    print(f"Class {i}")
    result = stat(N, data)
    print(f"Max {result[0]}, Min {result[1]}, Largest gap {result[2]}")