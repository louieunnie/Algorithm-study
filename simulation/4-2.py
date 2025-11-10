# 시각
# 예제 4-2 (이코테)
# Q. 0시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오

import sys
input = sys.stdin.readline

N = int(input())
# print("---ANSWER---")
cnt = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+"-"+str(m)+"-"+str(s):
                cnt += 1
print(cnt)