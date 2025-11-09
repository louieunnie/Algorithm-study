# 수학 & 통계 함수 모음

# 자주 쓰는 함수: sqrt(x), factorial(x), ceil(x)/floor(x), log(x, base), gcd(a, b), comb(n, k), perm(n, k) 

import math

print(math.sqrt(9)) # 제곱근 3.0
print(math.factorial(5)) # 팩토리얼 120
print(math.gcd(24, 18)) # 최대공약수 6
print(math.pi) # 3.1415926..
print(math.e) # 2.7182818..

# 예제
# 양의 정수 n이 주어질 때, 
# 1부터 n까지의 수 중에서 n과 서로소 (GCD=1)인 수의 개수를 반환하세요. 

import math

def count_coprimes(n):
    cnt = 0
    for i in range(n):
        if math.gcd(n, i+1) == 1:
            cnt += 1
    return cnt
print(count_coprimes(10))
# 4 (1, 3, 7, 9)