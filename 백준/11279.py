import heapq
import sys
input = sys.stdin.readline
N = int(input().rstrip())
heap = []
for i in range(N):
    q = int(input().rstrip())
    if q == 0 and len(heap) == 0:
        print(0)
    elif q == 0:
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-q, q))
