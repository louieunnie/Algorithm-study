# 반복자를 다루는 내장 라이브러리

# 자주쓰는 함수: product(), permutations(), combinations(), accumulate(), cycle()/repeat()
from itertools import permutations, combinations, accumulate
# permuations()- 순열: 리스트에서 순서를 고려하여 N개 선택
print(list(permutations([1, 2, 3], 2)))
# combinations()- 조합: 리스트에서 순서를 고려하지 않고 N개 선택
print(list(combinations([1, 2, 3], 2)))
# accumulate()- 누적합
print(list(accumulate([1, 2, 3, 4])))



# 예제
# 정수 리스트 arr과 정수 r이 주어질 때, 
# r개의 원소로 만들 수 있는 모든 조합의 합을 오름차순 리스트로 반환하세요

from itertools import combinations

def combination_sums(arr, r):
    return sorted([sum(c) for c in combinations(arr, r)])

print(combination_sums([1, 2, 3, 4], 2))