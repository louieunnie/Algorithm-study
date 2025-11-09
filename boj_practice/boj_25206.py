import sys

input = sys.stdin.readline

N = 20

score = {
    "A": 4,
    "B": 3, 
    "C": 2, 
    "D": 1, 
    "F": 0
}
total = 0
points = []
for i in range(N):
    name, point, grade = input().split()
    if grade == "P":
        continue
    else:
        points.append(float(point))
        if len(grade)== 1:
            sc = score[grade]
        elif len(grade) == 2:
            sc = score[grade[0]]
            if grade[1] == "+":
                sc += 0.5
    total += float(point) * sc
avg = total / sum(points)
print(f"{avg:.6}")
