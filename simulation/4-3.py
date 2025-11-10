# 왕실의 나이트
# 예제 4-3 (이코테)
# Q. 8 x 8 좌표 평면 상에서 현재 나이트가 위치한 좌표가 주어졌을 때, 
# 나이트가 이동할 수 있는 경우의 수를 출력하라. 
import sys

input = sys.stdin.readline

cur_loc = input().strip()
x_chess = "abcdefgh"
x_pos = x_chess.index(cur_loc[0])+1
y_pos = int(cur_loc[1])

move_x = [+1, +1, -1, -1, +2, +2, -2, -2]
move_y = [+2, -2, +2, -2, +1, -1, +1, -1]

now = x_pos, y_pos
cnt = 0
for i in range(len(move_x)):
    next_x = x_pos + move_x[i]
    next_y = y_pos + move_y[i]
    if 1 <= next_x <= 8:
        if 1 <= next_y <= 8:
            cnt += 1
print(cnt)
