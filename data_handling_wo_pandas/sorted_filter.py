# sorted() and filter() function practice

# sorted(iterable, key=None, reverse=False)

# Q1) 학생 리스트가 주어질 때, 점수가 높은 순으로 이름만 반환하라
def sort_students(students):
    result = sorted(students, key=lambda x:x[1], reverse=True)
    result = [x[0] for x in result]
    return result
print(sort_students([("A", 90), ("B", 70), ("C", 80)]))

# Q2) 직원 리스트 중 연봉이 5000 이상인 사람만 이름을 오름차순 정렬해서 반환하라
def high_salary(employees):
    result = sorted(employees, key = lambda x: x[0])
    result = [x[0] for x in result if x[1] >= 5000]
    return result

print(high_salary([("Ann", 4800), ("Ben", 5100), ("Cara", 6000)]))

# filter(function, iterable)
# function이 True를 반환하는 원소만 남김 -> filter 객체가 반환되므로 list() 변환 필요

# Q1) 짝수만 남기기 
def keep_even(nums):
    return list(filter(lambda x: x % 2 == 0, nums))
print(keep_even([1, 2, 3, 4, 5, 6]))

# Q2) 평균보다 높은 값만 남기기
def above_average(nums):
    return list(filter(lambda x: x > sum(nums)/len(nums), nums))

print(above_average([70, 80, 90, 100]))

## 합친 문제: 
# Q1) 학생들의 점수가 주어질 때, 상위 n명의 평균 점수를 구하세요. 
def top_average(scores, n):
    sort_result = sorted(scores, reverse = True)
    result = sum(sort_result[:n])/n
    return result
print(top_average([70, 90, 85, 100, 60], 3))

# Q2) 상품들의 (이름, 가격, 카테고리) 리스트가 주어질 때, 
# 카테고리가 "food"인 상품 중 가장 싼 상품 이름을 구하라

def cheapest_food(products):
    filtered = filter(lambda x: x[2] == "food", products)
    # sorted_ = sorted(filtered, key = lambda x: x[1])
    # return sorted_[0][0]
    cheapest = min(filtered, key=lambda x: x[1])
    return cheapest[0]
data = [
    ("apple", 1200, "food"),
    ("soap", 800, "daily"),
    ("bread", 1000, "food")
]
print(cheapest_food(data))

# Q3) 데이터 리스트가 주어질 때,
# 평균 ± 표준편차 범위를 벗어난 값을 제거하고
# 남은 데이터들을 오름차순으로 반환하라.

import math

def clean_data(data):
    avg = sum(data) / len(data)
    var = sum((d-avg)**2 for d in data)/len(data)
    std = math.sqrt(var)
    filtered = list(filter(lambda x: (avg-std) <= x <= (avg+std), data))
    return sorted(filtered)

print(clean_data([10, 12, 13, 50, 11, 10, 9]))