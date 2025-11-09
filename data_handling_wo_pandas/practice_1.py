# Q1) 숫자 리스트가 주어졌을 때 짝수만 제곱해서 합을 구하라
def sum_even_squares(arr):
    total = 0
    for n in arr:
        if n % 2 == 0:
            total += n**2
    return total

print(sum_even_squares([1, 2, 3, 4, 5, 6]))

## sum 내장함수 활용하기
def sum_even_squares(arr):
    return sum(x**2 for x in arr if x % 2 == 0)
print(sum_even_squares([1, 2, 3, 4, 5, 6]))

# Q2) 학생 점수 데이터에서 평균보다 높은 학생 이름을 추출하라
students = [
    {"name":"A","score":70},
    {"name":"B","score":90},
    {"name":"C","score":80}
]

avg = sum(x["score"] for x in students)/len(students)
answer = [x["name"] for x in students if x["score"] > avg]
print(answer)

# Q3) 상품 리스트를 가격 내림차순으로 정렬하라
items = [
    {"name":"apple","price":1200},
    {"name":"banana","price":800},
    {"name":"cherry","price":1500}
]


sorted_items = sorted(items, key = lambda x: x["price"], reverse= True)
print(sorted_items)

# Q4) 문자열 리스트에서 문자열을 정수로 바꾸고, 10보다 큰 값만 남기기
data = ["5", "20", "8", "15"]

result = list(filter(lambda x: x > 10, map(int, data)))
print(result)

# Q5) 학생별 과목 평균 구하기
grades = {
    "A": [80, 90, 100],
    "B": [70, 80, 90],
    "C": [60, 70, 80]
}
# print({k: v for k, v in grades.items()})
print({k: sum(v)/len(v) for k, v in grades.items()})