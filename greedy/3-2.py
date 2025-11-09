# 큰 수의 법칙
# 예제 3-1 (이코테)
# Q. N개의 자연수가 주어질 때, 주어진 수들을 M번 더하여 가장 큰 수를 만들어라. 
# 이때, 특정 인덱스의 번호를 K번 초과하여 더할 수 없다. 
# 2 <= N <= 1000, 1 <= M <= 10000, 1 <= K <= 10000

import sys

input = sys.stdin.readline

N, M, K = map(int, input().strip().split())

data = list(map(int, input().strip().split()))

data = sorted(data, reverse = True)
# print(data)
one_loop = data[0] * K + data[1]

num_of_loops = M // (K + 1)
residue = M % (K + 1)

ans = num_of_loops * one_loop + data[0] * residue


print(ans)
