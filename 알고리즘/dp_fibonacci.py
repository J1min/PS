fibo = [0] * 100
fibo[0], fibo[1], fibo[2] = 0, 1, 1


def 디피보나치(N):
    if N <= 1:
        return N
    if fibo[N] != 0:
        return fibo[N]
    fibo[N] = 디피보나치(N-1) + 디피보나치(N-2)
    return fibo[N]
