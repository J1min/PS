# PROBLEM - 
# TIER - G
# NUMBER - 7662
# DATE - 2022-07-31 15:25
# IDEA - 힙 관련 자료구조 문제이지만 시간제한이 6초임에도 자꾸 타임아웃;;
import heapq
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for i in range(T):
    N = int(input().rstrip())
    queue = []
    for j in range(N):
        command, value = input().split()
        value = int(value)
        if command == "D" and len(queue) > 0:
            if value == -1:  # 젤작은값 삭제
                heapq.heappop(queue)
            else:  # 젤큰값 삭제
                queue.pop(queue.index(max(queue)))
        elif command == "I":  # 값 넣기
            heapq.heappush(queue, value)
    if len(queue) == 0:
        print("EMPTY")
    else:
        print(max(queue), min(queue))
