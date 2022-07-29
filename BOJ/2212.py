# PROBLEM - 센서
# NUMBER - 2212
# DATE - 2022-07-29 00:18
# IDEA - 그리디로 정렬한 뒤에 최소값을 찾는 문제이다.
# 가장 큰 차이들을 잘라줌으로서 가장 작은 거리끼리 합쳐줬다

import sys
N = int(input())
M = int(input())
distance = sorted(list(map(int, input().split())))
gap = []
if M >= N:
    print(0)
    sys.exit()

for i in range(N-1):
    gap.append(distance[i+1] - distance[i])

gap.sort()
for i in range(M-1):
    gap.pop()
print(sum(gap))
