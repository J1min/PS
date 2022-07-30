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

for i in range(N):
    time = list(map(int, input().split()))
    # if time[1] - time[0] == 0:
    #     count += 1
    # else:
    times.append(time)

times.sort(key=lambda x: (x[1], x[0]))
count = 0
start = times[0][0]
end = times[0][1]
times.pop(0)
while True:
    # print(times)
    if len(times) == 0:
        break
    for i in range(len(times)-1):
        if times[i][0] == times[i][1]:
            count += 1
            break
        if times[i+1][0] >= end:
            start = times[i+1][0]
            end = times[i+1][1]
            count += 1
    times.pop(0)
print(count+1)