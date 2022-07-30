import sys
# PROBLEM - 전생했더니 슬라임 연구자였던 건에 대하여 (Hard)
# TIER - G4
# NUMBER - 14698
# DATE - 2022-07-30 15:21
# IDEA - 곱했을 때의 값을 최소로 만들어주는
# 일반적인 정렬 + 그리디로 예상됨

import heapq
input = sys.stdin.readline

T = int(input().rstrip())
for i in range(T):
    N = int(input().rstrip())
    slaimu = sorted(list(map(int, input().split())))
    heapq.heapify(slaimu)
    if N == 1:
        print(1)
        continue
    total = []
    while True:
        if len(slaimu) == 1:
            break
        a, b = heapq.heappop(slaimu), heapq.heappop(slaimu)
        heapq.heappush(slaimu, a*b)
        total.append(a*b)
        answer = 1
    for i in range(N-1):
        answer *= (total[i] % 1000000007)
    print(answer)
