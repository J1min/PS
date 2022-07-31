# PROBLEM - 피보나치 함수 
# TIER - S3
# NUMBER - 19598
# DATE - 2022-07-31 13:29
# IDEA - dp로 피보나치 구현후에 0, 1 카운팅하는 문제인데 이거 좀 이상하긴 함 어케함;
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def dpibonacci(N):
    global c0
    if N == 0:
        c0 += 1
    if fibo[N] != 0:
        return fibo[N]
    else:
        fibo[N] = dpibonacci(N-1) + dpibonacci(N-2)
        return [c0, fibo[N]]

N = int(input().rstrip())
fibo = [0] * 100
fibo[0], fibo[1], fibo[2] = 0, 1, 1

for i in range(N):
    c0 = 0
    print(dpibonacci(int(input().rstrip())))
