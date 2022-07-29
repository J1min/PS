import sys
# PROBLEM - 구간 합 구하기 4
# TIER - S3
# NUMBER - 11659
# DATE - 2022-07-29 18:08
# IDEA - 너무 쉬워보여서 풀어볼려고는 하는데 좀 쎄함
# 알고보니까 누적 합 [1, 2, 3, 4, 5] => [1, 3, 6, 10, 15]
# 이런식으로 해준다음에 주는 인덱스의 요소들끼리 빼기하면 되는거엿노 ㅋㅋ

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
prefix = [0] * N
temp = 0

for i in range(N):
    temp += numbers[i]
    prefix[i] = temp
prefix = [0]+prefix

for i in range(M):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a-1])

