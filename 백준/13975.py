import queue

heap = queue.PriorityQueue()

N = int(input())
for i in range(N):
    M = int(input())
    numbers = list(map(int, input().split()))
    