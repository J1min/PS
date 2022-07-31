import sys
# PROBLEM - 파일 합치기 3
# TIER - G4
# NUMBER - 13975
# DATE - 2022-07-30 18:21
# IDEA - 그리디
# 이건 내일 풀거긴 한데 이거 아무리 봐도
# 힙 써서 최소값(힙으로 쓰는 배열 제일 처음 값) 계속 pop 해가면서 재끼는 문제

import heapq
input = sys.stdin.readline
answer = []
N = int(input().rstrip())
numbers = [int(input().rstrip()) for _ in range(N)]
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
