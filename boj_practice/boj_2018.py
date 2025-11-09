# import sys

# input = sys.stdin.readline

# N = int(input().strip())
# data = [i for i in range(1, N+1)]
# cnt = 0
# for w in range(1, N+1):
#     # print("w: ", w)
#     window = sum(data[:w])
#     # print("window: ", window)
#     if window == N:
#         cnt += 1
#     for i in range(w, N):
#         window = window +data[i] - data[i-w]
#         if window == N:
#             cnt += 1
        
# print(cnt)

import sys

input = sys.stdin.readline

N = int(input().strip())
# data = [i for i in range(1, N+1)]
cnt = 0
for w in range(1, N+1):
    # print("w: ", w)
    window = 0
    for i in range(w):
        window += i
    # print("window: ", window)
    if window == N:
        cnt += 1
    for i in range(w, N):
        window = window +i - (i-w)
        if window == N:
            cnt += 1
        
print(cnt)