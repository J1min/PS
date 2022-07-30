import sys
# PROBLEM - 두 배 더하기
# TIER - G5
# NUMBER - 12931
# DATE - 2022-07-30 15:07
# IDEA - 그리디로 할것
    # 핵심 아이디어는 
    # 모든 수가 짝수인 경우 => //= 2
    # 하나라도 홀수가 있으면 홀수 골라서 -= 1
input = sys.stdin.readline
N = int(input().rstrip())
target = list(map(int, input().split()))
count = 0

def is_odd(array):
    for i in range(N):
        if array[i] % 2 == 1:
            return False
    return True

while sum(target) > 0:
    status = is_odd(target)
    # print(target)
    if status: # 모두 짝수인 경우엔
        for i in range(N):
            target[i] //= 2
        count += 1
    else:
        for i in range(N):
            if target[i] % 2 == 1:
                target[i] -= 1
                count += 1

print(count)
