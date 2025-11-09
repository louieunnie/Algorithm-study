import sys

input = sys.stdin.readline

C = int(input())

def get_ratio(N, arr):
    avg = sum(arr)/N
    above_avg = [x for x in arr if x > avg]
    ratio = len(above_avg)/N *100
    return ratio

for _ in range(C):
    data = list(map(int, input().split()))
    N = data[0]
    data = data[1:]

    result = get_ratio(N, data)
    print(f"{result:.3f}%", end = "\n")