# 이진 탐색!
# 정렬된 배열에서 특정 원소를 찾아야하 ㄹ때 효과적으로 사용됨
# 자주 쓰는 함수: bisect_left(a, x), bisect_right(a, x)
# 시간 복잡도 O(logN)

from bisect import bisect_left, bisect_right

arr = [1, 2, 4, 4, 8]

x = 4
# 1. bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음
print(bisect_left(arr, x)) # 2 반환

# 2. bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾음
print(bisect_right(arr, x)) # 4 반환


## 두 함수를 이용해서, 정렬된 리스트에서 값이 [left_value, right_value]에 속하는 데이터의 개수를 반환하는 함수 구현 가능
## 시간복잡도 O(logN)
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index-left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4)) # 2
print(count_by_range(a, -1, 3)) # 6

# 예제
# 정렬된 리스트 arr에서 x가 들어갈 인덱스를 반환하세요.
# 단, 이미 존재하면 기존 값의 오른쪽 위치로 들어가야 합니다. 
import bisect

def insert_position(arr, x):
    return bisect.bisect_right(arr, x)
print(insert_position([1, 3, 3, 5, 7], 3))