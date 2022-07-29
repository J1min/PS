# PROBLEM - 강의실 배정
# NUMBER - 11000
# DATE - 2022-07-28 23:53
# IDEA - 아까 증감배열인지 뭔지랑 똑같은 양산형 문제인듯

N = int(input())
times = []
for i in range(N):
    start, end = map(int, input().split())
    times.append([start, 1])
    times.append([end, -1])
times.sort()

count = 0
max_ = 0

for A, B in times:
    count += B
    if B == 1:
        max_ = max(max_, count)

print(max_)