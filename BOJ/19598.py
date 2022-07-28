# PROBLEM - 최소 회의실 개수
# NUMBER - 19598
# DATE - 2022-07-28 21:11
# IDEA - 그리디 문제입니다 아마 최대회의실 배정처럼
# 이제 이어지는거끼리 이어주고 남는거끼리 남기고 이런식으로 갈듯
import sys
input = sys.stdin.readline

N = int(input().rstrip())
time = list()
room = []

for i in range(N):
    time.append(list(map(int, input().split())))
time.sort()


while True:
    if len(time) == 0:
        break
    now = []
    pop_list = []
    now.append(time.pop(0))
    for i in range(len(time)):
        if now[0][1] <= time[i][0]:
            now.append(time[i])
            pop_list.append(i)
    for i in pop_list:
        time.pop(i)
    room.append(now)


print(len(room))
print(room)
