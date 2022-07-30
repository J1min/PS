# PROBLEM - 강의실 배정
# NUMBER - 11000
# DATE - 2022-07-28 23:53
# IDEA - 힙 사용하는 양산형 문제입니다.
import heapq

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort()

heap = []
heapq.heappush(heap, times[0][1])
for i in range(1, N):
    start, end = times[i][0], times[i][1]
    if heap[0] > start: # 끝나는 시간중에 제일 빠른 것 보다 시작시간이 더 빠를 경우
        heapq.heappush(heap, end) # 강의실 추가
    else: # 강의실 연강 가능한 경우 (끝나는 시간이 더 짧은 강의가 들어온 경우)
        heapq.heappop(heap) # 제일 짧은 강의 삭제
        heapq.heappush(heap, end) # 그리고 제일 짧은 강의 (맨 앞에) 추가
print(len(heap)) # heappop이 맨 앞에있는 친구를 날리는 듯