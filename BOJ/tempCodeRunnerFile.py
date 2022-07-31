
import heapq
input = sys.stdin.readline
answer = []
N = int(input().rstrip())
numbers = [int(input()) for _ in range(N)]
heapq.heapify(numbers)
while True:
    if len(numbers) <= 1:
        print(sum(answer))
        break
    min_ = heapq.heappop(numbers)
    max_ = heapq.heappop(numbers)
    result = min_ + max_
    heapq.heappush(numbers, result)
    answer.append(result)
