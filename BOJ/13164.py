import sys
# PROBLEM - 행복 유치원
# TIER - G5
# NUMBER - 13164
# DATE - 2022-07-30 13:50
# IDEA - 그리디 입니다

# N명의 학생들을 M개의 그룹으로 나눈다고 했을 때 
# 달리 말하면 N-M 개의 키 차이를 무시할 수 있다는 것이다.

# 그러니까 한 팀인 사람들을 2개의 팀으로 분리시키면 
# 키 차이가 1개 무시가 되잖아 그 말임

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
gap = []
for i in range(N-1):
    gap.append(numbers[i+1] - numbers[i])
gap.sort()
print(sum(gap[:N-M]))