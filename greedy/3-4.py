# 1이 될 때까지
# 예제 3-4 (이코테)

import sys

input = sys.stdin.readline
N, K = map(int, input().strip().split())
cnt = 0
while True:
    if N == 1:
        break
    if N % K == 0:
        N = N // K 
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)

# 정답 풀이
# result = 0
# while N >= K:
#     while N % K != 0:
#         N-=1
#         result += 1
#     N // = k
#     result += 1
# while N > 1:
#     N-= 1
#     result += 1
# print(result)

# 더 빠르게 동작하게 하려면 (중요중요)
# result = 0
# while True:
#     target = (N//K) *K 
#     result += (N-target)
#     N = target
#     if N < K:
#         break
#     result += 1
#     N //= K
# result += (N-1)
# print(result)