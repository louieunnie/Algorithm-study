import sys
from collections import Counter
input = sys.stdin.readline

N, L = map(int, input().strip().split()) # N: 줄 길이, L: 경사로 길이

data = []
streets= []
# 데이터 저장 및 가로 계산
for i in range(N):
    row = list(map(int, input().strip().split()))
    data.append(row)
    street = True
    cntr = dict(Counter(row))
    if len(cntr) == 1:
        streets.append(street)
        continue
    # print(f"row {i+1}-------")
    for j in range(N-1):
        # print(row[j])
        if row[j]-row[j+1] == 1:
            # print("here")
            # print(f"row{i+1}: {j}-{j+1}")
            for l in range(1, L+1):
                if j + l > N-1:
                    # print("here5")
                    street = False
                    break
                if row[j+1]!=row[j+l]:
                    # print('here6')
                    street=False
                    break
                if j + L + 1 < N:
                    if row[j] == row[j+L+1]:
                        street=False
                        break          
        elif row[j]-row[j+1] == -1:
            # print("here2")
            # print("j: ", j)
            for l in range(1, L):
                # print(j-l)
                if j - l < 0:
                    # print("here3")
                    street= False
                    break
                if row[j]!=row[j-l]:
                    # print('here4')
                    street=False
                    break
                if j-L >=0:
                    if row[j+1]== row[j-L]:
                        street=False
                        break
        elif abs(row[j]-row[j+1]) > 1:
            # print("here10")
            street= False
            break
        
    # print(f"street?:{street}" )
    streets.append(street)
print(streets)
print(streets.count(True))

# 세로
streets2= []

# 데이터 저장 및 가로 계산
for i in range(N):
    col = [x[i] for x in data]
    street = True
    print(f"col {i+1}-------")
    print(col)
    cntr = dict(Counter(col))
    if len(cntr) == 1:
        streets2.append(street)
        print(f"street?:{street}" )
        continue
    for j in range(N-1):
        print(col[j])
        if col[j]-col[j+1] == 1:
            print("here")
            print(f"col{i+1}: {j}-{j+1}")
            for l in range(1, L+1):
                if j + l > N-1:
                    print("here5")
                    street = False
                    break
                if col[j+1]!=col[j+l]:
                    print('here6')
                    street=False
                    break
                if j + L + 1 < N:
                    if col[j] == col[j+L+1]:
                        street=False
                        break        
        elif col[j]-col[j+1] == -1:
            print("here2")
            print("j: ", j)
            for l in range(1, L):
                print(j-l)
                if j - l < 0:
                    print("here3")
                    street= False
                    break
                if col[j]!=col[j-l]:
                    print('here4')
                    street=False
                    break
                if j-L >= 0:
                    if col[j+1]== col[j-L]:
                        street=False
                        break
        elif abs(col[j]-col[j+1]) > 1:
            print("here10")
            street= False
            break
    print(f"street?:{street}" )
    streets2.append(street)
print(streets2)
print(streets2.count(True))
ans = streets.count(True) + streets2.count(True)
print(ans)