import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().strip().split())

data = []
place = {
    "house": [],
    "chicken": []
}
for i in range(N):
    row = list(map(int, input().strip().split()))
    data.append(row)
    for j in range(len(row)):
        if row[j] == 1:
            place["house"].append((i+1, j+1))
        elif row[j] == 2:
            place["chicken"].append((i+1, j+1))

possible_ch = list(combinations(place["chicken"], M))
dists = []
for case in possible_ch:
    total = 0
    for h in place["house"]:
        minimum = N * 2
        h_x, h_y = h
        for c in case:
            c_x, c_y = c
            dist = abs(h_x - c_x) + abs(h_y-c_y)
            if dist < minimum:
                minimum = dist
        total += minimum
    dists.append(total)
print(min(dists))

