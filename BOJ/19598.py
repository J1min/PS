import sys
# PROBLEM - 최소 회의실 개수
# TIER - G5
# NUMBER - 19598
# DATE - 2022-07-29 22:29
# IDEA - 
# 로직 자체는 간단하다
# 일단 자동으로 정렬이 되는 힙을 통해서
# 시작시간이 끝나는 시간보다 
input = sys.stdin.readline

import heapq

n = int(input().rstrip())

lecture_list = [list(map(int, input().split())) for _ in range(n)]
lecture_list.sort()

lecture_queue = []
heapq.heappush(lecture_queue, lecture_list[0][1])
print(lecture_queue)
for i in range(1, n):
    if lecture_list[i][0] < lecture_queue[0]:
        heapq.heappush(lecture_queue, lecture_list[i][1])
    else:
        heapq.heappop(lecture_queue)
        heapq.heappush(lecture_queue, lecture_list[i][1])
print(lecture_queue)
print(len(lecture_queue))