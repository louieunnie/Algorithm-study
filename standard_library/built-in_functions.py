# 파이썬 내장함수: 라이브러리 import 없이 바로 사용 가능한 기본 함수

# 20개 주요 내장함수
# sum, len, max, min, round, abs, sorted, enumerate, map, filter, zip, range, list, dict, str, type, isinstance, any, all, print

# 1. sum(): 합계 계산
scores = [70, 80, 90]
print(sum(scores)) # 240
print(sum(x**2 for x in scores)) # 70^2 + 80^2 + 90^2 =19400

# 2. len(): 길이(개수)
data = ["a", "b", "c"]
print(len(data)) # 3

# 3. max(), min(): 최댓값, 최솟값
nums = [3, 10, 5]
print(max(nums)) # 10
print(min(nums)) # 3

## lambda 활용
students = [{"name": "A", "score": 90}, {"name": "B", "score": 80}]
print(max(students, key=lambda x: x["score"])) # {"name": "A", "score": 90}
print(max(students, key=lambda x:x["score"])["name"]) # A

# 4. round() 반올림
print(round(3.14159)) # 3
print(round(3.14159, 4)) # 3.1416
print(round(2.675, 2)) # 2.67

## 부동소수점과 Decimal
# 파이썬 (혹은 대부분의 프로그래밍 언어)는 실수를 2진수(이진 부동소수점)으로 저장함
# 따라서 10진수의 대부분의 소수를 정확히 표현할 수 없음

# 즉, 2.675는 실제로 메모리에 다음처럼 저장됨 
# => 2.6749999999999998

# 따라서, round(2.6749999999999998, 2) → 2.67

# 올바르게 반올림하고 싶을때, 10진수 단위 계산을 위해 Decimal로 계산함

from decimal import Decimal, ROUND_HALF_UP
x = Decimal('2.675') # 정확히 10진수로 저장
print(x.quantize(Decimal('0.01'), rounding = ROUND_HALF_UP))

# 프린트 때만 잘 나오게 하려면
print(f"{Decimal('2.675'):.2f}")

# 6. abs(): 절댓값
print(abs(-10)) # 10
print(abs(3-8)) # 5

# 7. sorted() : 리스트, 딕셔너리 등 정렬
nums = [3, 1, 4]
print(sorted(nums))  #[1, 3, 4]
print(sorted(nums, reverse = True))  # [4, 3, 1]

records = [{"name": "A", "score": 70}, {"name": "B", "score": 90}]
print(sorted(records, key=lambda x: x["score"], reverse = True)) # [{'name': 'B', 'score': 90}, {'name': 'A', 'score': 70}]

# 8. enumerate(): 인덱스와 값을 함께 순회
names = ["Alice", "Bob", "Charlie"]
for idx, name in enumerate(names):
    print(idx, name)
# 0 Alice / 1 Bob / 2 Charlie

for idx, name in enumerate(names, start =1):
    print(idx, name)
# 1 Alice / 2 Bob / 3 Charlie

# 9. map(): 모든 원소에 함수 적용
nums = ["1", "2", "3"]
nums = list(map(int, nums)) # 리스트의 모든 원소에 int 적용
print(nums) # [1, 2, 3]

print((map(lambda x: x **2, [1, 2, 3]))) # <map object at 0x0000014F3E233EB0>
print(list(map(lambda x: x**2, [1, 2, 3]))) # [1, 4, 9]

# 10. filter(): 조건 만족하는 원소만 남기기
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x%2 == 0, nums)) # nums의 원소 중 원소 x %2가 0인 원소만을 남겨 리스트 만듦
print(even)

# 11. zip(): 여러 리스트 묶기
names = ["A", "B", "C"]
scores = [90, 80, 70]
pairs = list(zip(names, scores))
print(pairs)  # # [('A',90),('B',80),('C',70)]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# A: 90 / B: 80 / C: 70

# 12. range(): 반복 범위 만들기
for i in range(3):
    print(i) # 0 /1 /2

arr = [i**2 for i in range(1, 6)]
print(arr) # [1, 4, 9, 16, 25]

# 13: list(): 리스트 변환
text = "abc"
print(list(text)) # ['a', 'b', 'c']

data = {1, 2, 3}
print(list(data)) # [1, 2, 3]

# 14: dict(): 딕셔너리 생성 또는 변환

pairs = [("A", 90), ("B", 80)]
print(dict(pairs)) # {'A':90, 'B':80}

## 딕셔너리 초기화
d = dict(name= "Alice", age = 25)
print(d["name"]) # Alice

# 15: str(): 문자열 변환
num = 123
print("The number is " + str(num)) # The number is 123

# 16: type(): 자료형 확인
x= [1, 2, 3]
print(type(x)) # <class 'list'>

# 17: isinstance(): 자료형 검사
x = [1, 2, 3]
print(isinstance(x, list)) # True
print(isinstance(x, dict)) # False

# 18: any(): 하나라도 True면 True 반환
arr = [0, False, 3, 0]
print(any(arr)) # True (3이 True여서)
print(any(x > 4 for x in arr)) # False (x>4 를 만족하는 원소가 없어서)

# 19: all(): 모두 True여야 True 반환
arr = [1, 2, 3]
print(all(x > 0 for x in arr)) # True (모든 원소가 0보다 크므로)
print(all(x < 3 for x in arr)) # False (3은 3보다 작지 않으므로)

# 20: print(): 출력
print("Hello", "World", sep = ", ") # Hello, World
print("Hello", "World", sep = ", ", end = "!\n") # Hello, World!



## 예제: 평균보다 높은 점수를 가진 학생 찾기
students = [{"name": "A", "score": 80}, {"name": "B", "score": 90}, {"name": "C", "score": 70}]

## 평균 구하기
avg = sum(x["score"] for x in students)/len(students) # 80.0
print([x["name"] for x in students if x["score"] > avg]) # B