import sys
# PROBLEM - 회의실 배정
# TIER - S1
# NUMBER - 1931
# DATE - 2022-07-29 22:29
# IDEA - 그리디 입니다
# 약간 내 생각에는 회의시간이 짧은 순으로 끼워맞추면 어떨까 하는데..

input = sys.stdin.readline
N = int(input().rstrip())
times = []
gap = []

for i in range(N):
    times.append(list(map(int, input().split())))

for i in range(N):
    gap.append(times[i][1] - times[i][0])

# times.sort()
# gap.sort()
print(times)
print(gap)
