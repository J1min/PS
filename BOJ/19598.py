import sys
# PROBLEM - 최소 회의실 개수
# TIER - G5
# NUMBER - 19598
# DATE - 2022-07-29 22:29
# IDEA - 힙으로날먹 ㅋㅋ
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

for i in range(1, N):
    if time[i][0] < queue[0]: # 만약 시작시간이 현재 제일 먼저 끝나는 시간보다 작을 경우
        heapq.heappush(queue, time[i][1]) # 기존 회의실 사용
    else: # 강의 2개가 겹친 경우 새로운 회의실 개설
        heapq.heappop(queue)
        heapq.heappush(queue, time[i][1])
print(len(queue))
