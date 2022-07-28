import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    q = int(sys.stdin.readline())
    if q == 0 and len(heap) == 0:
        print(0)
    elif q == 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, q)
    