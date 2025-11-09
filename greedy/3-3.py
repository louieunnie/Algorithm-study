# 숫자 카드 게임
# 예제 3-3 (이코테)

import sys

input = sys.stdin.readline
N, M = map(int, input().strip().split())

# 최소수가 가장 큰 row를 선택하여 최대 수를 선택해야 함
max_min = 0
for i in range(N):
    row = list(map(int, input().strip().split()))
    minimum = min(row)
    if minimum > max_min:
        max_min = minimum

ans = max_min
print(ans)
