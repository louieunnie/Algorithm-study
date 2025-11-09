# 확장된 자료구조

# 자주 쓰는 구조
## 1) deque : 양방향 큐 (O(1)의 시간복잡도로 pop/append) -> BFS, 시뮬레이션
## 2) Counter : 원소 개수 카운트 -> 빈도 개산
## 3) defaultdict : 기본값 있는 딕셔너리

from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))


# Counter: 리스트와 같은 ITERABLE 객체가 주어졌을 때, 해당 객체 내부 원소의 등장 횟수를 셈
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 변환

# 예제
# 문자열 s의 각 문자가 몇 번 등장했는지를 딕셔너리 형태로 반환하세요.

from collections import Counter

def char_count(s):
    return dict(Counter(s))

print(char_count("banana"))