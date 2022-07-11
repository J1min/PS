import heapq
# 반정렬 배열임
# 트리모양

heap = []

heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 4)
heapq.heappush(heap, 5)

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

heapq.heappush(heap, (-1, 1))
heapq.heappush(heap, (-2, 2))
heapq.heappush(heap, (-3, 3))
heapq.heappush(heap, (-4, 4))
heapq.heappush(heap, (-5, 5))

print(heapq.heappop(heap)[1])
print(heapq.heappop(heap)[1])
print(heapq.heappop(heap)[1])
print(heapq.heappop(heap)[1])
print(heapq.heappop(heap)[1])