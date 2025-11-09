import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split()) # N: 포켓몬 수, M: 문제 수

num_to_name= {}
name_to_num = {}
for i in range(1, N+1):
    name = input().strip()
    num_to_name[i] = name
    name_to_num[name] = i

for j in range(M):
    query = input().strip()
    try:
        query = int(query)
        print(num_to_name[query])
    except:

        print(name_to_num[query])