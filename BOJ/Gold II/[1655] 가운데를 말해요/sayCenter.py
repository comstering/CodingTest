import sys
import heapq

n = int(sys.stdin.readline())

right_heap = []
left_heap = []
mid = int(sys.stdin.readline())
print(mid)

for _ in range(n - 1):
    num = int(sys.stdin.readline())
    if num > mid:
        heapq.heappush(right_heap, num)
        if len(right_heap) > len(left_heap) + 1:
            heapq.heappush(left_heap, (-mid, mid))
            mid = heapq.heappop(right_heap)
    else:
        heapq.heappush(left_heap, (-num, num))
        if len(left_heap) > len(right_heap):
            heapq.heappush(right_heap, mid)
            mid = heapq.heappop(left_heap)[1]

    print(mid)
