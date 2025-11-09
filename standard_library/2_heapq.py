# 최소 힙 기반 우선순위 큐

# 자주 쓰는 함수: heappush(heap, item), heappop(heap), heapify(list)
# 파이썬의 heap은 minheap으로 구성되어서, 단순히 원소를 힙에 넣었다 빼면
# 시간복잡도 O(NlogN)의 오름차순 정렬이 완료됨!

import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 2, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
# 최대 힙은 없기 때문에 원소의 부호를 임시로 변경하는 방식을 사용함
# 이를 이용해서 오름차순 정렬 구현
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# 예제
# 정수 리스트 arr에서 가장 작은 k개의 수를 오름차순으로 반환하세요

import heapq

def k_smallest(arr, k):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(k)]

print(k_smallest([8, 3, 5, 1, 6], 3))
# [1, 3, 5]