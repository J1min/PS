# PROBLEM - 수 찾기
# NUMBER - 1920
# DATE - 2022-07-28 17:32
# IDEA - 이분탐색의 기본중에 기본. 수를 찾고 있는지 없는지 반환
# 집합으로도 풀 수는 있지만 그냥 연습겸 함해보죠
import sys

def binary(array, start, end, target):
    if start > end:
        return 0
    mid = (start+end)//2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary(array, start, mid-1, target)
    else:
        return binary(array, mid+1, end, target)


N = int(sys.stdin.readline().rstrip())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline().rstrip())
search = (list(map(int, sys.stdin.readline().split())))

for i in range(M):
    print(binary(numbers, 0, M-1, search[i]))
