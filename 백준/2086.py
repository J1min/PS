fibo = [0] * 100
fibo[0], fibo[1], fibo[2] = 0, 1, 1


def dp(T, T1):
    if T1 <= 1:
        return 1
    if fibo[T1] == 0:
        fibo[T1] = dp(T1-1) + dp(T1-2)
    return fibo[T1]


T, T1 = map(int, input().split())
print(dp(T, T1))
