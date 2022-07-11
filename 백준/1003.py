

def dp(N):
    if N <= 1:
        count[N] += 1
        return 1
    if fibo[N] != 0:
        return fibo[N]
    else:
        return dp(N-1) + dp(N-2)
    return fibo[N]


T = int(input())
fibo = [0] * (T+3)
fibo[0], fibo[1], fibo[2] = 0, 1, 1
count = [0, 0]
count[1] = fibo[-1]+fibo[-2]
print(dp(T))
print(count)