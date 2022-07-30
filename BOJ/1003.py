import sys
# PROBLEM - 
# TIER - G
# NUMBER - 19598
# DATE - 2022-07-29 22:29
# IDEA - 

def dp(N):
    global zeroCount
    result = []
    fibo = [0] * 50
    fibo[0], fibo[1] = 1, 1
    if N == 0:
        zeroCount += 1
    if fibo[N] != 0:
        return fibo[N]
    else:
        fibo[N] = dp(N-1) + dp(N-2)
    return fibo[N]

N = int(input())
zeroCount = 0
for i in range(N):
    q = int(input())
    print(dp(q))
