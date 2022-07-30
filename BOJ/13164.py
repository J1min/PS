import sys
# PROBLEM - 행복 유치원
# TIER - G5
# NUMBER - 13164
# DATE - 2022-07-30 13:50
# IDEA - 그리디 입니다
#
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
gap = []
for i in range(N-1):
    gap.append(numbers[i+1] - numbers[i])
gap.sort()
print(sum(gap[:N-M]))