import sys
# PROBLEM - 강의실
# TIER - G5
# NUMBER - 1374
# DATE - 2022-07-30 14:34
# IDEA - 웰논데수 
# 힙을 통해 날먹을 해보죠

import heapq
input = sys.stdin.readline
queue = []
time = []
N = int(input().rstrip())
for i in range(N):
    start, end = map(int, input().split())
    time.append([start, end])
time.sort()
heapq.heappush(queue, time[0][1]) # 일단 제일 처음 시작하는 강의는 힙에 넣고

for i in range(1, N): # 그 다음 강의부터 for 문으로 처리
    if time[i][0] < queue[0]: # 만약 시작시간이 현재 제일 먼저 시작하는 시간보다 작을 경우
        heapq.heappush(queue, time[i][1]) # 기존 회의실 사용
    else: # 새로운 회의실 개설
        heapq.heappop(queue) # 
        heapq.heappush(queue, time[i][1])
print(len(queue))

# 단, 이 때 종료시간이 빠른 회의실부터 다음 회의를 이어서 개최해야 하기 때문에
# 우선순위 큐를 이용해 큐에 push를 해주어 큐가 정렬상태를 유지할 수 있도록 해준다.
