# 상하좌우
# 예제 4-1 (이코테)
# Q. 공간의 크기 N X N과 여행가가 이동할 계획서 내용이 주어질 때, 
# 여행가가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

N = int(input().strip())
directions = list(input().strip().split())

map_ = [[] for _ in range(N)]

for i in range(0, N):
    map_[i].extend((i+1, j) for j in range(1, N + 1))

move = {
    "U": (-1, 0),
    "D": (+1, 0),
    "L": (0, -1),
    "R": (0, +1)
}
now = (1, 1)

for i in range(len(directions)):
    next = tuple(sum(x) for x in zip(now, move[directions[i]]))
    if 0 < next[0] < N and 0 < next[1] < N:
        now = next
    else:
        continue
print(now[0], now[1])

# 답안 예시

